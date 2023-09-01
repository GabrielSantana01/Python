Na Arvore de decisão temos que saber quais critérios que avaliam o grau de impureza dos nossos atributos

temos os seguintes criterios:

indice Gine
Qui-quadrado
Ganho de informação(Entropia)
Redução na variância


o indice Gine verifica a probabilidade de ocorrer a classe para cada feature existente. quando fazemos a verificação de todas as features temos 
quais features tem maior influencia do resultado da classe. entao usamos essas features para criar a arvore de decisão.
a função consiste em multiplicar a probabilidade de ocorrer a classe com a subitração de não ocorrer a classe com 1 = Pk*(1-Pk)
o indice Gine tem o foco de verificar a impureza dos dados, ou seja quanto mais proximo de 1 estiver os dados mais impuro a feature(eterogenia) é para identificar a classe.
quanto mais proximo a feature ficar de 0 mais homogenia ela vai ser. logo usamos ela para fazer a arvore.

Ja a Entropia mede a ordenação dos dados para detectar sua impureza, verifica o ganho de informação (conseito que devo estudar ainda)
E = - somatorio Pk*log(Pk) base=2

from sklearn.tree import DecisionTreeClassefier # importa a biblioteca
dtc = DecisionTreeClassifier(criterion='entropy', random_state=42) # instancia o modelo escolhendo o criterio e colocando o random_state
dtc.fit(x_treino, y_treino) # treino meus dados
dtc.feature_importances_#verifica a variavel mais importante
predito_ArvoreDecisao = dtc.predict(x_teste)
