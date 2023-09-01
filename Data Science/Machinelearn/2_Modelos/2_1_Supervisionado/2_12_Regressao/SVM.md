
train_x = é a variavel que vai armazenar todas as features
train_y = é a classificação real do item para treino


test_x = é a variavel que vai armazenar todas as features reservado para teste.
test_y = é a classificação real do item para teste.

usando a biblioteca  sklearn vamos importar o modelo de machine learn LinearSVC

from sklearn.svm import LinearSVC
model = LinearSVC()# instanciamos a classe LinearSVC da biblioteca sklearn no objeto model

model.fit(train_x, train_y) e usamos como parametro o train_x como dados e o train_y como classe

com isso nosso modelo esta treinado. apartir desse treino o nosso modelo deve ser capaz de criar previsões 
para isso vamos para a parte do teste.

usamos uma variavel chamada previsões que usa como referencia as features do test_x para gerar uma classificação estimada dos itens.
previsoes = model.predict(test_x)
Com a variavel previsoes obtendo a classificação estimada iremos comparar a taxa de acerto dessas previsões com a classificação 
de teste real(test_y). 
from aklearn.metrica import accuracy_score

taxa_de_acerto = accuracy_score(test_y, previsoes)

o codigo acima nos retorna a porcentagem de acetos que tivemos com o nosso modelo. isso é feito comparando o teste_Y com a previsoes
----------------------------------------------------------------------------------------------------------------------------------

existe um metodo na biblioteca sklearn responsavel por dividir as amostras de treino(x) e teste(y) é o: train_test_split() 
random_state = O estado aleatório que você fornece é usado como uma semente para o gerador de números aleatórios. 
Isso garante que os números aleatórios sejam gerados na mesma ordem.




from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
url = "https://gist.githubusercontent.com/guilhermesilveira/2d2efa37d66b6c84a722ea627a897ced/raw/10968b997d885cbded1c92938c7a9912ba41c615/tracking.csv"
pd.read_csv(uri)
x= dados[["home","how_it_works","contact"]]
y= dados[["bought"]]
SEED = 45 
train, test_x, train_y, test_y =train_test_split(x, y, random_state = SEED, test_size =0.25)
modelo = LinearSVC()
modelo.fit(treino_x, treino_y)
previsoes = modelo.predict(teste_x)

acuracia = accuracy_score(teste_y, previsoes) * 100
------------------------------------------------------------------------------------------------------------------------------------
temos que garantir que o algoritmo de ML seja melhor do que um chute ao acaso. logo se ela tiver um percentual baixo quer dizer que o 
modelo aplicado não é o melhor para o caso. podemos compara se a porcentagem do nosso modelo com uma previsao ao acaso usando o numpy.
criando assim o conceito da linha de base. que nada mais é do que o valor minimo que nosso modelo tem que ultrapassar para ser considerado
bom.

import numpy as np 
baseline = np.ones(len(x_test))
acuracia = accuracy_score(teste_y, baseline) * 100
-------------------------------------------------------------------------------------------------------------------------------------
SVC = support vector classification
SVM = support vector machine


