KNN - Modelo K-Nearest Neighbors ()
o modelo segue os seguintes passos:
 - recebe as informações
 - Calcula as Distâncias
 - Ordena a distância da menor para a maior
 - Realiza contagem de quantas classes existe
 - classifica a partir dos k-maens

K pequeno pode ocorrer overfitting = o modelo vai se ajustar perfeitamente aos dados de entrada. e nao vai classificar corretamente novos dados 
K grande underfitting = vai criar muitas classes e nao vai identificar a classe correta dos novos clientes.

implantando modelo:

temos os dados da nova cliente, a Maria. logo xMaria é a variavel com todos os valores das features da maria.
Xmaria = [[0,0,1,1,0,0,39.90,1,0,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,1]]
bom abaixo vamos serpara nossas features de nossa classe. isso que esses dados ainda não tem os valores da Maria.
X = dados_final.drop('Churn', axis = 1)
Y = dados_final['Churn']

metrica de distancia:
para calcularmos a distancia de Maria com os demais clientes temos que deixar todos os valores na mesma escala

usamos a biblioteca abaixo para preprocessar os dados. com ela definimos distancias entre os itens.
from sklearn.preprocessing import StandardScaler
norm = StandardScaler()
x_normalizado = norm.fit_transform(x)
x_normalizado

aplicamos uma escala para os dados da maria tb. para isso tranformamos os dados da maria em DataFrame e defimimos que as colunas desse
DataFreme vai ser a mesma que as colunas do DataFrame de X.
Xmaria_normalizado = norm.transform(pd.DataFrame(Xmaria, columns = X.columns))

agora vamos verificar a distancia da maria para os demais clientes:

import numpy as np
a = Xmaria_normalizado
b = X_normalizado[0]
a - b

np.sqrt(84.07574038273466)
a distância da Maria com o cliente 0 da nossa base, é 9.169282435541762
