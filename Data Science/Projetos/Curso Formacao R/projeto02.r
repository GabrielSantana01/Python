# Define o diretório de trabalho
setwd("/home/gabrielux/Python/Data Science/Projetos/Curso Formacao R/")

# Verifica o diretório de trabalho atual
print(getwd())
# Carrega os pacotes readr e dplyr
library(readr)
library(dplyr)

x <- c(30.5, 35.3,33.2,40.3,41.5,36.3,43.2,34.6,38.5)
y <- c(28.2,35.1,33.2,35.6,40.2,37.4,34.2,42.1,30.5,38.4)
resultado <- t.test(x,y,conf.level =0.95, paired=t)

print(resultado)