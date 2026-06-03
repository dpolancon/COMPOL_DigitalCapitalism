library(readr)
library(quanteda)
library(quanteda.textplots)
library(text2vec)
library(tidytext)
library(tidyverse)
library(ggplot2)
library(lubridate)
library(seededlda)
library(data.table)
library(tinytex)
library(knitr)
library(stringi)
library(stringr)
library(base)
library(fastDummies)


# Construcción de la Base de Datos y Caracteristicas Principales


#Clear all 
rm(list = ls())


## Ruta para las bases de datos 
ruta ="C:/Users/dpola/Dropbox/datos_tesis_chicholina"
#Ruta Chicho
#ruta ="C:/Users/dpola/Dropbox/datos_tesis_chicholina"



#Abrimos bases de datos (anuncions FB) 

#vendepatria 
boric <- read_csv(paste0(ruta,"/boric.csv"))
boric$candidato <- "Boric"
boric$vuelta <- 1

#vendepatria orden y progreso
boric_2V <- read_csv(paste0(ruta,"/boric_2V.csv"))
boric_2V$candidato <- "Boric"
boric_2V$vuelta <- 2

#meo 
meo <- read_csv(paste0(ruta,"/meo.csv"))
meo$candidato <- "MEO"
meo$vuelta <- 1

#sichel 
sichel <- read_csv(paste0(ruta,"/sichel.csv"))
sichel$candidato <- "Sichel"
sichel$vuelta <- 1

#Yasnagol 
yasna <- read_csv(paste0(ruta,"/yasnagol.csv"))
yasna$candidato <- "Yasna"
yasna$vuelta <- 1

#Kakas
kast <- read_csv(paste0(ruta,"/kast.csv"))
kast$candidato <- "Kast"
kast$vuelta <- 1

#Kast 2nda vuelta 
kast_2V <- read_csv(paste0(ruta,"/kast_2V.csv"))
kast_2V$candidato <- "Kast"
kast_2V$vuelta <- 2

#Hacemos un stack de las bases 
lista<-ls()
data <- rbind.data.frame(boric,boric_2V,kast,kast_2V,meo,sichel,yasna)
rm(list=lista)

#eliminamos var sin texto 
data <- data %>%  drop_na(c("ad_creative_bodies","demographic_distribution")) 



#Creamos variable de izquierda y derecha 1era vuelta. 
list_izq = c("Boric","MEO","Yasna")
list_der = c("Sichel","Kast")
data <- data %>%  mutate(izq_der = case_when(vuelta==1 & (candidato %in% list_izq) ~ 1, 
                                             vuelta==1 & (candidato %in% list_der) ~ 2))



#Creamos variables de segmentacion demografica 

data <- data %>%  mutate(izq_der = case_when(vuelta==1 & (candidato %in% list_izq) ~ 1, 
                                             vuelta==1 & (candidato %in% list_der) ~ 2))

rm(list_izq,list_der)


#Limpiamos emojis del corpus 
only_ascii_regexp <- '[^\u0001-\u007F]+|<U\\+\\w+>'
data$ad_creative_bodies <- data$ad_creative_bodies %>% str_replace_all(regex(only_ascii_regexp), "") 


#creamos un corpus para df_1v 
corpus <- data$ad_creative_bodies %>%  corpus()


#Añadimos ariables de la base de datos al corpus de texto  
docvars(corpus) <- data

#Tokenizamos
tok_data <- tokens(corpus)

## Decisiones de pre-processing 
#Removemos puntos  
tok_data <- tokens(tok_data, remove_punct = TRUE)

#Remover Numeros  
tok_data <- tokens(tok_data, remove_numbers = TRUE)

#Remover Simbolos  
tok_data <- tokens(tok_data, remove_symbols = TRUE)

#Solo minusculas (decapitalization)
tok_data <- tokens_tolower(tok_data)

#Stopwords en español 
tok_data <- tokens_select(tok_data, pattern = stopwords("es"),  selection = "remove")

#ngrams 
tok_data <- tokens_ngrams(tok_data,n = 1)

#Remover palabras claves 
list_remover <- c("vota","presidente","facebook","gabriel","boric",
                  "yasna","provoste", "jose","kast","sebastian","http://aportes.servel.cl",
                  "sichel", "marco","enriquez","enriquez-ominami","ominami","mas","ms","chile","si","https://bit.ly/3arjjiz",
                  "enrquez-ominami","@laterceracom","https://boricpresidente.cl/apoderados",
                  "@evelynmatthei","@pdazan","https://bit.ly/39qz1ty","l")

tok_data <- tokens_remove(tok_data, pattern = list_remover, padding = FALSE)
#tok_data <- tokens_remove(tok_data, pattern = regex(only_ascii_regexp), padding = FALSE)

#Doc Feature Matrix
dfm_data <-dfm(tok_data)
rm(tok_data)


Ktopic = 10


#creamos las dummies de topicos 
dmt  <-  data %>%  filter(vuelta==1) 
dmt$id <- 1:nrow(dmt)
topic_mt <-  dfm_data %>%  dfm_subset(vuelta==1) %>% textmodel_lda(k =Ktopic) %>% topics()
dmt$topics <- topic_mt
dmt <- select(dmt, c('id','topics')) 
dmt_t <- table(dmt$topics)/sum(table(dmt$topics))
dmt_t <-as.data.frame(dmt_t)
colnames(dmt_t)<-c("topics","t_pbb")
dmt_f <- merge(dmt,dmt_t)
dmt_f <-dmt_f %>% arrange(id)

#dmt <- dummy_cols(dmt, select_columns = 'topics')
#dmt=as.data.frame(dmt)

#limpiamos y reshapiamos la segmentacion demografica
dem  <-  data %>%  filter(vuelta==1) 
dem <- str_split(dem$demographic_distribution,'[{}]')
dem <- lapply(dem, function(dem) dem[!grepl("^,", dem)])
dem <- lapply(dem, function(dem) dem[!grepl("^*$", dem)])

#Limpiamos segmentacion 
st_rep <- function(x) {
  x = str_replace_all(x,":" ,"")
  x = str_replace_all(x,"\"" ,"")
  x = str_replace_all(x,"age","")
  x = str_replace_all(x,"gender","")
  x = str_replace_all(x,"percentage","")
  x = str_replace_all(x,"percent","")
  x = str_split(x,",",simplify = TRUE)
}
dem <- lapply(dem,st_rep)
dem <- mapply(cbind, dem, "id"=1:length(dem), SIMPLIFY=T)
dem <- do.call(rbind, dem)
colnames(dem)[1:3]<-c("edad","genero","p")
dem=as.data.frame(dem)


#Tabla edad 
dem$p <- as.numeric(dem$p)
aux1 <- dem %>% group_by(id,edad) %>% summarise(p_c = sum(p))
aux1 <- merge(dmt_f,aux1)
aux1 <- dummy_cols(aux1, select_columns = c("topics"))
aux1 <- dem %>% arrange(id,edad)
tabla_edad = matrix(,nrow=7,ncol = Ktopic)
for (x in 1:Ktopic){ 
  X.varname <- paste0("T_",x)
  Topic.varname<-paste0("topics_topic",x)
  aux1 <- aux1  %>% mutate(!!X.varname := eval(parse(text=Topic.varname))*p_c*t_pbb)
  ddd <- aux1 %>% group_by(edad) %>% summarise(!!X.varname := 100*mean(eval(parse(text=X.varname))))
  tabla_edad[,x] <- as.matrix(ddd[2])
}
oo = unique(aux1$edad)[7]
ii = unique(aux1$edad)[1:6]
rownames(tabla_edad) <- c(oo,ii)

#Tabla genero 
dem$p <- as.numeric(dem$p)
aux1 <- dem %>% group_by(id,genero) %>% summarise(p_c = sum(p))
aux1 <- merge(dmt_f,aux1)
aux1 <- dummy_cols(aux1, select_columns = c("topics"))
aux1 <- dem %>% arrange(id,genero)
tabla_genero = matrix(,nrow=3,ncol = Ktopic)
for (x in 1:Ktopic){ 
  X.varname <- paste0("T_",x)
  Topic.varname<-paste0("topics_topic",x)
  aux1 <- aux1  %>% mutate(!!X.varname := eval(parse(text=Topic.varname))*p_c*t_pbb)
  ddd <- aux1 %>% group_by(genero) %>% summarise(!!X.varname := 100*mean(eval(parse(text=X.varname))))
  tabla_genero[,x] <- as.matrix(ddd[2])
}
rownames(tabla_genero) <- c("Mujer","Hombre","Desconocido")


#juntamos tedad y tgenero 
tabla_mt <- rbind(tabla_edad,tabla_genero)
colnames(tabla_mt) <- paste0("T", 1:Ktopic)   
tabla_mt

######Region
#limpiamos y reshapiamos la segmentacion regional 
aux <- str_split(data$delivery_by_region,'[{}]')
aux <- lapply(aux, function(aux) aux[!grepl("^,", aux)])
aux <- lapply(aux, function(aux) aux[!grepl("^*$", aux)])

#Limpiamos reg 
st_rep <- function(x) {
  x = str_replace_all(x,":" ,"")
  x = str_replace_all(x,"\"" ,"")
  x = str_replace_all(x,"region","")
  x = str_replace_all(x," Region","")
  x = str_replace_all(x,"percentage","")
  x = str_replace_all(x,"percent","")
  x = str_split(x,",",simplify = TRUE)
}
aux <- lapply(aux,st_rep)
reg = aux 

