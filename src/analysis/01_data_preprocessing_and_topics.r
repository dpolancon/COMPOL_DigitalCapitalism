# ==============================================================================
# PROJECT: Data-Driven Microtargeting: Chile 2021
# FILE: 01_data_preprocessing_and_topics.R
# PURPOSE: Data loading, text preprocessing, demographic parsing, and LDA 
#          topic modeling for all analysis subsets defined in the Analytical 
#          Foundation memo.
# ==============================================================================

library(tidyverse)
library(quanteda)
library(quanteda.textplots)
library(textclean)
library(jsonlite)
library(stringi)

# ------------------------------------------------------------------------------
# 1. DATA LOADING & METADATA CREATION
# ------------------------------------------------------------------------------
# Note: Update 'ruta' to point to your local data directory.
ruta <- "data/raw/" 

load_candidate <- function(file, cand_name, round) {
  path <- paste0(ruta, file)
  if (!file.exists(path)) {
    warning(paste("File not found:", path))
    return(NULL)
  }
  df <- read_csv(path, show_col_types = FALSE)
  df$candidato <- cand_name
  df$vuelta <- round
  return(df)
}

candidates <- list(
  list(file = "boric.csv", name = "Boric", round = 1),
  list(file = "boric_2V.csv", name = "Boric", round = 2),
  list(file = "meo.csv", name = "MEO", round = 1),
  list(file = "sichel.csv", name = "Sichel", round = 1),
  list(file = "yasnagol.csv", name = "Yasna", round = 1),
  list(file = "kast.csv", name = "Kast", round = 1),
  list(file = "kast_2V.csv", name = "Kast", round = 2)
)

data_list <- map(candidates, ~ load_candidate(.x$file, .x$name, .x$round))
data <- bind_rows(data_list) %>%
  drop_na(ad_creative_bodies, demographic_distribution) %>%
  mutate(
    ad_id = row_number(), # Unique ID for each ad
    bloc = case_when(
      candidato %in% c("Boric", "MEO", "Yasna") ~ "Left",
      candidato %in% c("Sichel", "Kast") ~ "Right",
      TRUE ~ "Other"
    )
  )

cat("Total ads loaded:", nrow(data), "\n")

# ------------------------------------------------------------------------------
# 2. TEXT PREPROCESSING & CORPUS BUILDING
# ------------------------------------------------------------------------------
# Clean text: remove hashtags, emojis, normalize to ASCII
data$ad_text <- data$ad_creative_bodies %>%
  replace_hash() %>%
  replace_emoji() %>%
  stringi::stri_trans_general("latin-ascii")

# Create quanteda corpus
corp <- corpus(data, text_field = "ad_text")
docvars(corp) <- data %>% select(ad_id, candidato, vuelta, bloc)

# Tokenization and cleaning
toks <- tokens(corp, remove_punct = TRUE, remove_numbers = TRUE, remove_symbols = TRUE) %>%
  tokens_tolower() %>%
  tokens_remove(pattern = stopwords("es")) %>%
  tokens_ngrams(n = 1)

# Custom removal list (candidate names, URLs, common noise)
custom_remove <- c(
  "vota", "presidente", "facebook", "gabriel", "boric", "yasna", "provoste", 
  "jose", "kast", "sebastian", "sichel", "marco", "enriquez", "ominami", 
  "enriquez-ominami", "enrquez-ominami", "chile", "http", "https", "bit", 
  "ly", "latercera", "evelynmatthei", "pdazan", "apoderados", "voto", 
  "eleccion", "election", "programa", "propuesta"
)
toks <- tokens_remove(toks, pattern = custom_remove)

# Create Document-Feature Matrix (DFM)
dfm_obj <- dfm(toks)
cat("DFM created:", nfeat(dfm_obj), "features,", ndoc(dfm_obj), "documents.\n")

# ------------------------------------------------------------------------------
# 3. DEMOGRAPHIC DATA PARSING (Robust JSON/Regex Hybrid)
# ------------------------------------------------------------------------------
# Parses the FB Ads Library demographic_distribution into the exact 21 cells 
# defined in the Analytical Foundation memo.

ages <- c("13-17", "18-24", "25-34", "35-44", "45-54", "55-64", "65+")
genders <- c("male", "female", "unknown")
all_segments <- expand.grid(age = ages, gender = genders) %>%
  mutate(segment = paste(age, gender, sep = "_")) %>%
  pull(segment)

parse_demographics <- function(json_str) {
  if (is.na(json_str) || json_str == "") return(tibble())
  
  parsed <- tryCatch({
    # Try standard JSON parsing first
    p <- fromJSON(json_str)
    if (is.data.frame(p)) p else bind_rows(p)
  }, error = function(e) {
    # Fallback regex for malformed FB API exports (e.g., missing commas)
    ages_ext <- str_extract_all(json_str, '(?<="age":")[^"]+')[[1]]
    genders_ext <- str_extract_all(json_str, '(?<="gender":")[^"]+')[[1]]
    percs_ext <- str_extract_all(json_str, '(?<="percentage":)[0-9.]+')[[1]]
    if(length(ages_ext) > 0) {
      tibble(age = ages_ext, gender = genders_ext, percentage = as.numeric(percs_ext))
    } else {
      tibble()
    }
  })
  
  if (nrow(parsed) == 0) return(tibble())
  
  parsed %>%
    mutate(
      age = tolower(age),
      gender = case_when(
        gender %in% c("male", "hombre", "m") ~ "male",
        gender %in% c("female", "mujer", "f") ~ "female",
        TRUE ~ "unknown"
      ),
      segment = paste(age, gender, sep = "_")
    ) %>%
    select(segment, percentage) %>%
    pivot_wider(names_from = segment, values_from = percentage, values_fill = 0)
}

cat("Parsing demographic distributions...\n")
demo_list <- map(data$demographic_distribution, parse_demographics)

demo_wide <- bind_rows(demo_list, .id = "row_id") %>%
  mutate(ad_id = as.integer(.id)) %>%
  select(-.id)

# Ensure all 21 segments exist as columns
for (seg in all_segments) {
  if (!(seg %in% colnames(demo_wide))) demo_wide[[seg]] <- 0
}

demo_wide <- demo_wide %>% select(ad_id, all_of(all_segments), everything())

# Normalize rows to sum to 1 (handling FB API rounding issues)
row_sums <- rowSums(demo_wide[, all_segments])
demo_wide[, all_segments] <- demo_wide[, all_segments] / row_sums

cat("Demographic parsing complete.\n")

# ------------------------------------------------------------------------------
# 4. TOPIC MODELING (LDA) ACROSS ALL SUBSETS
# ------------------------------------------------------------------------------
# Defines the 11 subsets required by the Analytical Foundation memo
subsets_config <- list(
  list(name = "R1_All", filter = data$vuelta == 1),
  list(name = "R1_Left", filter = data$vuelta == 1 & data$bloc == "Left"),
  list(name = "R1_Right", filter = data$vuelta == 1 & data$bloc == "Right"),
  list(name = "R1_Boric", filter = data$vuelta == 1 & data$candidato == "Boric"),
  list(name = "R1_MEO", filter = data$vuelta == 1 & data$candidato == "MEO"),
  list(name = "R1_Yasna", filter = data$vuelta == 1 & data$candidato == "Yasna"),
  list(name = "R1_Sichel", filter = data$vuelta == 1 & data$candidato == "Sichel"),
  list(name = "R1_Kast", filter = data$vuelta == 1 & data$candidato == "Kast"),
  list(name = "R2_All", filter = data$vuelta == 2),
  list(name = "R2_Boric", filter = data$vuelta == 2 & data$candidato == "Boric"),
  list(name = "R2_Kast", filter = data$vuelta == 2 & data$candidato == "Kast")
)

K <- 10 # Number of topics (maintaining continuity with legacy qualitative interpretation)

run_lda_subset <- function(subset_name, filter_logic) {
  cat(paste0("Processing subset: ", subset_name, "...\n"))
  dfm_sub <- dfm_subset(dfm_obj, filter_logic)
  
  if (ndoc(dfm_sub) < K) {
    warning(paste("Subset", subset_name, "has fewer documents than K. Skipping."))
    return(NULL)
  }
  
  lda_model <- textmodel_lda(dfm_sub, k = K)
  
  top_terms <- terms(lda_model, 10) %>%
    as.data.frame() %>%
    rownames_to_column("topic_id") %>%
    pivot_longer(-topic_id, names_to = "rank", values_to = "term") %>%
    mutate(subset = subset_name)
    
  map_topics <- tibble(
    ad_id = as.integer(docnames(dfm_sub)),
    map_topic = topics(lda_model)
  ) %>% mutate(subset = subset_name)
    
  return(list(model = lda_model, terms = top_terms, assignments = map_topics))
}

lda_results <- map(subsets_config, ~ run_lda_subset(.x$name, .x$filter))
names(lda_results) <- map_chr(subsets_config, "name")

all_top_terms <- bind_rows(map(lda_results, "terms"))
all_assignments <- bind_rows(map(lda_results, "assignments"))

cat("Topic modeling complete.\n")

# ------------------------------------------------------------------------------
# 5. QUALITATIVE INTERPRETATION DICTIONARY (From Legacy Thesis)
# ------------------------------------------------------------------------------
# Use this table to map the arbitrary LDA topic_id (1-10) to your established 
# qualitative labels by matching the top terms in 'all_top_terms'.

topic_labels_reference <- tibble(
  subset = c(rep("R1_All", 6), rep("R1_Left", 6), rep("R1_Right", 4), 
             rep("R1_Boric", 6), rep("R1_MEO", 3), rep("R1_Yasna", 4), 
             rep("R1_Sichel", 5), rep("R1_Kast", 6), rep("R2_All", 7), 
             rep("R2_Boric", 7), rep("R2_Kast", 5)),
  label = c(
    "Pensiones", "Reforma de salud", "Educación de calidad", "Seguridad pública", "Derechos de las mujeres", "Cambios/Gobierno",
    "Cuarto retiro", "Pensiones", "Empleo femenino", "Salud", "Educación", "Seguridad",
    "Mujeres emprendedoras", "Políticas de discapacidad", "Esfuerzo familiar", "Pensiones",
    "Apoyo a pymes", "Educación no sexista", "Pensiones", "Cuidado de niños", "Sustentabilidad", "Reforma de salud",
    "Impuesto al combustible", "Reactivación económica", "Seguridad",
    "Pensiones", "Empleo", "Seguridad pública", "Reactivación económica",
    "Mujeres emprendedoras", "Discapacidad", "Experiencia", "Seguridad", "Futuro",
    "Fortalecer familia", "Terrorismo", "Delincuencia", "Áreas verdes", "Paz social", "Violencia",
    "Migración", "Apoyo a pymes", "Mujeres", "Orden", "Narcotráfico", "Elites políticas", "Seguridad",
    "Apoyo a pymes", "Migración", "Delincuencia", "Policías", "Narcotráfico", "Igualdad de género", "Apoyo a agricultores",
    "Orden público", "Inmigración", "Género", "Narcotráfico", "Paz social"
  )
)

# ------------------------------------------------------------------------------
# 6. SAVE OUTPUTS FOR NEXT STAGE
# ------------------------------------------------------------------------------
dir.create("data/processed", showWarnings = FALSE)

# 1. Clean data with parsed 21-cell demographic matrix
data_clean <- data %>%
  select(ad_id, candidato, vuelta, bloc, ad_text) %>%
  left_join(demo_wide, by = "ad_id")

write_rds(data_clean, "data/processed/data_clean.rds")

# 2. LDA models and top terms for interpretation
saveRDS(list(
  models = map(lda_results, "model"),
  top_terms = all_top_terms,
  labels_reference = topic_labels_reference
), "data/processed/lda_models_and_terms.rds")

# 3. MAP topic assignments for all subsets (Required for REI/TTD/TGC indices)
write_rds(all_assignments, "data/processed/topic_assignments.rds")

cat("All processed data saved to 'data/processed/'.\n")
cat("Ready for 02_indices_calculation.R\n")