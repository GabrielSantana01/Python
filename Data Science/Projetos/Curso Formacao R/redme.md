sudo apt install r-base
R --version
install.packages("nome_do_pacote")

Persistência de Pacotes: Para garantir que os pacotes instalados sejam persistentes, você pode criar um arquivo .Rprofile no seu diretório home com configurações personalizadas.

install.packages("readr")  # Execute isso apenas uma vez para instalar o pacote
library(readr)