# ==============================================================================
# PROJECT: Data-Driven Microtargeting: Chile 2021
# FILE: 00_master_scaffold_v2.R
# PURPOSE: Strict implementation of the locked "Analytical Foundation" memo
# ==============================================================================

library(tidyverse)
library(quanteda)
library(topicmodels)
library(ineq)

# ------------------------------------------------------------------------------
# 1. BASELINE DEMOGRAPHIC DISTRIBUTION
# ------------------------------------------------------------------------------
# LOCKED MATH: \bar{P}_s = \frac{1}{A_q} \sum P_{a,s}
# NOTE: This is an UNWEIGHTED mean across ads. Every ad counts as 1.

compute_baseline_demo <- function(ads_data, demo_col = "demo_proportions") {
  # ads_data must have a list-column where each element is a named numeric 
  # vector of proportions for each segment summing to 1.
  
  demo_matrix <- do.call(rbind, ads_data[[demo_col]])
  
  # Unweighted mean across ads (columns are segments)
  baseline_demo <- colMeans(demo_matrix, na.rm = TRUE)
  
  return(baseline_demo)
}

compute_conditional_demo <- function(ads_data, topic_assignments, demo_col = "demo_proportions") {
  # topic_assignments: vector of length nrow(ads_data) with MAP topic k
  
  demo_matrix <- do.call(rbind, ads_data[[demo_col]])
  unique_topics <- sort(unique(topic_assignments))
  
  conditional_baselines <- map_dfr(unique_topics, function(k) {
    idx <- which(topic_assignments == k)
    if(length(idx) > 0) {
      props <- colMeans(demo_matrix[idx, , drop = FALSE], na.rm = TRUE)
      tibble(topic_id = k, segment = names(props), prop = props)
    } else {
      tibble(topic_id = k, segment = character(), prop = numeric())
    }
  })
  
  return(conditional_baselines)
}

# ------------------------------------------------------------------------------
# 2. INDEX 1: RELATIVE EXPOSURE INDEX (REI)
# ------------------------------------------------------------------------------
# LOCKED MATH: REI_{s,k} = \bar{P}_{s|k} / \bar{P}_s

calculate_rei_panel <- function(cond_baselines_df, baseline_demo) {
  cond_baselines_df %>%
    mutate(baseline = baseline_demo[segment]) %>%
    mutate(rei = prop / baseline) %>%
    # Handle division by zero if baseline segment is 0
    mutate(rei = ifelse(is.infinite(rei) | is.nan(rei), NA, rei)) %>%
    select(topic_id, segment, rei)
}

# ------------------------------------------------------------------------------
# 3. INDEX 2: TOPIC TARGETING DIVERGENCE (TTD)
# ------------------------------------------------------------------------------
# LOCKED MATH: TTD_k = JSD(P_{.|k} || P_{.}) using log_2. Domain [0,1].
# CORRECTION: Removed sqrt(). Enforced base-2 logarithm.

jsd_base2 <- function(p, q) {
  p <- p / sum(p)
  q <- q / sum(q)
  m <- 0.5 * (p + q)
  
  # Handle zeros to avoid log(0)
  eps <- 1e-15
  p[p == 0] <- eps; q[q == 0] <- eps; m[m == 0] <- eps
  
  # Renormalize
  p <- p / sum(p); q <- q / sum(q); m <- m / sum(m)
  
  kl_pm <- sum(p * log2(p / m))
  kl_qm <- sum(q * log2(q / m))
  
  return(0.5 * kl_pm + 0.5 * kl_qm)
}

calculate_ttd_panel <- function(cond_baselines_df, baseline_demo) {
  cond_baselines_df %>%
    group_by(topic_id) %>%
    summarise(
      TTD = jsd_base2(prop, baseline_demo[segment]),
      .groups = "drop"
    )
}

# ------------------------------------------------------------------------------
# 4. INDEX 3: TARGETING GINI COEFFICIENT (TGC)
# ------------------------------------------------------------------------------
# LOCKED MATH: Standard population Gini of the conditional distribution vector.

calculate_tgc_panel <- function(cond_baselines_df) {
  cond_baselines_df %>%
    group_by(topic_id) %>%
    summarise(
      TGC = ineq(prop, type = "Gini", correct = FALSE), 
      .groups = "drop"
    )
}

# ------------------------------------------------------------------------------
# 5. CROSS-ROUND TOPIC MATCHING (Topic Birth/Death)
# ------------------------------------------------------------------------------
# LOCKED MATH: Cosine similarity between topic-word distributions (phi).

compute_cross_round_similarity <- function(beta_round1, beta_round2) {
  # beta matrices: Rows = Topics (K), Cols = Vocabulary (V)
  # Normalize rows to unit vectors for cosine similarity
  beta1_norm <- beta_round1 / sqrt(rowSums(beta_round1^2))
  beta2_norm <- beta_round2 / sqrt(rowSums(beta_round2^2))
  
  # Cosine similarity matrix (K1 x K2)
  sim_matrix <- beta1_norm %*% t(beta2_norm)
  
  return(sim_matrix)
}

classify_topic_evolution <- function(sim_matrix, tau_high = 0.80, tau_low = 0.30) {
  # Classify Round 2 topics based on max similarity to Round 1
  max_sim_for_r2 <- apply(sim_matrix, 2, max)
  r2_status <- case_when(
    max_sim_for_r2 >= tau_high ~ "Persistent",
    max_sim_for_r2 < tau_low   ~ "Birth",
    TRUE                       ~ "Transformed"
  )
  
  # Classify Round 1 topics based on max similarity to Round 2
  max_sim_for_r1 <- apply(sim_matrix, 1, max)
  r1_status <- case_when(
    max_sim_for_r1 >= tau_high ~ "Persistent",
    max_sim_for_r1 < tau_low   ~ "Death",
    TRUE                       ~ "Transformed"
  )
  
  list(
    round2_evolution = tibble(round2_topic = 1:ncol(sim_matrix), max_sim = max_sim_for_r2, status = r2_status),
    round1_evolution = tibble(round1_topic = 1:nrow(sim_matrix), max_sim = max_sim_for_r1, status = r1_status),
    similarity_matrix = sim_matrix
  )
}

# ------------------------------------------------------------------------------
# 6. PANEL CONSTRUCTION
# ------------------------------------------------------------------------------
# LOCKED MATH: Topic Summary Panel sorted by TTD descending.

build_topic_summary_panel <- function(rei_df, ttd_df, tgc_df, topic_labels, N_k_counts) {
  ttd_df %>%
    left_join(tgc_df, by = "topic_id") %>%
    left_join(N_k_counts, by = "topic_id") %>%
    left_join(topic_labels, by = "topic_id") %>%
    # Get argmax and max REI for each topic
    left_join(
      rei_df %>%
        group_by(topic_id) %>%
        summarise(
          max_REI_segment = segment[which.max(rei)],
          max_REI_value = max(rei, na.rm = TRUE),
          .groups = "drop"
        ),
      by = "topic_id"
    ) %>%
    # LOCKED MATH: "Columns are ordered by TTD_k descending"
    arrange(desc(TTD)) %>%
    select(topic_id, Label, N_k, TTD, TGC, max_REI_segment, max_REI_value)
}