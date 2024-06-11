# Dados
fumantes <- c(215, 190, 282, 186, 184, 231, 240, 230, 178, 219, 166, 199, 221, 176, 225, 213)
nao_fumantes <- c(221, 171, 165, 234, 224, 205, 256, 239, 180, 183, 217, 199, 298, 173, 267, 248)

# Teste t para duas amostras independentes
resultado <- t.test(fumantes, nao_fumantes, conf.level = 0.95)

# Exibe o resultado do teste t
print(resultado)
