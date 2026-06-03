
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


#Creamos variable de izquierda y derecha 1era vuelta. 
list_izq = c("Boric","MEO","Yasna")
list_der = c("Sichel","Kast")
data <- data %>%  mutate(izq_der = case_when(vuelta==1 & (candidato %in% list_izq) ~ 1, 
                                             vuelta==1 & (candidato %in% list_der) ~ 2))

#Creamos variables de segmentacion demografica 

data <- data %>%  muta

te(i
aux[[1]]
zq_der = case_when(vuelta==1 & (candidato %in% list_izq) ~ 1, 
                                             vuelta==1 & (candidato %in% list_der) ~ 2))


aux <-  str_split(data$demographic_distribution,'{\"age\":\"')

aux <-  str_split(aux,':')

#simplify=TRUE
{\"age\":\"25-34\",\"gender\":\"unknown\",\"percentage\":0.001109}

aux[[1]]

data$demographic_distribution[1]