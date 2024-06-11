# Define o diretório de trabalho
setwd("/home/gabrielux/Python/Data Science/Projetos/Curso Formacao R/")

# Verifica o diretório de trabalho atual
print(getwd())

# Instala os pacotes readr e dplyr se não estiverem instalados
if (!require(readr)) {
  install.packages("readr")
  library(readr)
}

if (!require(dplyr)) {
  install.packages("dplyr")
  library(dplyr)
}
if (!require(ggplot2)) {
  install.packages("ggplot2")
  library(ggplot2)
}

# Carrega os pacotes readr e dplyr
library(readr)
library(dplyr)

# Lê o arquivo CSV
dados <- read.csv("/home/gabrielux/Python/Data Science/Projetos/Curso Formacao R/dados.csv")

# Visualiza as primeiras linhas dos dados
print("Primeiras linhas dos dados:")
print(head(dados))

# Visualiza as últimas linhas dos dados
print("Últimas linhas dos dados:")
print(tail(dados))

# Exibe a estrutura do DataFrame
print("Estrutura dos dados:")
print(str(dados))

# Exibe um resumo estatístico dos dados
print("Resumo estatístico dos dados:")
print(summary(dados))
