na validação do modelo podemos ultilizar a matriz confusão para ter 3 tipos de validação:
acuracia
precisão
recall


matriz confusão:

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_teste, predito_knn))
print(confusion_matrix(y_teste, predito_ArvoreDecisao))
------------------------------------------------------------------------------
TP = True Positive
TN = True Negative
FP = False Positive
FN = False Negative
acuracia = "ACC = TP + TN/TP + FP + TN + FN"

from sklearn.metrics import accuracy_score
print(accuracy_score(y_teste, predito_knn))
print(accuracy_score(y_teste, predito_bnb))


--------------------------------------------------------------------------------
na validação temos as metricas de validação interna(não precisa de classe, não utilizam rótulos verdadeiros (ground truth)) 
e a metrica de validação externa(nescessita de classe)

metrica se baseiam em criterio de validação temos 2 principais 
Criterio de Validação: compactação --> nos diz quão proximos estao os pontos dentro de um mesmo cluster.

Criterio de Validação: separação --> nos diz quão bem separados estão os pontos em clusters diferentes.

para verificar o coeficiente de silhouette  = quanto mais proximo de 1 melhor
a = Criterio de Validação: compactação
    criamos uma tabela com as distancias de cada ponto pertencente a um cluster. usamos os valores de x e y da tabela
    para medir a distancia Euclidiana. com isso sabemos a distancia do ponto A para o ponto B. d(A, B) = raiz quadrada((xc -xa)2 + (yc -ya)2)
    sabendo o valor da distancia de A para B e de A para C temos que somar todas as distancias e divitir pela quantidade de vezes que a distancia foi calculada. dando assim a media.
    essa media corresponde ao valor de a, na formula original.
b = distancia media entre o ponto e todos os outros pontos do cluster. mais proximo. utilizamos o mesmo processo feito para achar a.

s = (b - a)/max(a,b)

o coeficiente de silhouette é uma tecinica de validação por separação(ou seja quanto maior o resultado melhor esta a separação)
é tambem um tipo de metrica de validação interna pois não precisa de rotulos verdadeiros(ground truth)
--------------------------------------------------------------------------------------------------------------------------------------------
existe outra metrica baseada em validação interna chamada de Davies-Bouldin = quanto menor melhor

sua compactação calcula a distancia dos elementos para o centro do cluster. e cria uma media para essas distancia.

fórmula abaixo é utilizada para medir a similaridade entre dois clusters i e j. Quanto menor o valor final mais similares são os clusters.
Desse modo, sabemos que s mede a compactação dos clusters e d mede a separação entre eles.

Rij = (Si + Sj)/Dij
---------------------------------------------------------------------------------------------------------------------------------------------
indice Calinski-Harabasz = quanto maior melhor

tr(Bk) = dispersão entre do (Between)clusters
tr(Wk) = dispersão dentro (within)clusters
k = numero de clusters 
Ne = numeros de elementos do clusters

s = ((tr(Bk)/tr(Wk)) x ((Ne-k)/(k-1)))

Validação Relativa:
foi feito uma verificação na alteração da quantidade de clusters para ver o impacto que era gerado na qualidade do indice
e atravez disso descidir a quantidade de clusters que vai ter no nosso modelo. como 5 clusters teve o melhor indice para 
o silhouette, acabamos escolhendo ele, pois o indice silhouette é um dos mais utilizados e vamos nos basear nele.

nesse analise foi alterado a quantidade de clusters para o modelo e foi visto que não ocorreu muita alteração 
na validação dos modelos. com 20 clusters e ate mesmo 50 clusters deve uma queda na qualidade dos indices.

--------------------------------------------------------------------------------------------------------------------
Valores aleatorios:
uma outra forma de validar se o idice de validação retornado do nosso modelo é bom ou não seria fazermos uma validação 
baseado em dados com valores aleatorios. com isso criariamos uma linha tendo como base o resultado desses indicies para 
os valores aleadorios e validariamos os nossos indices. caso nao tenha muita diferença de um indice feito com valores reais
dos valores aleatorios quer dizer que muita coisa esta errada.
essa tecnica tambem é usada para medir a acuracia do modelo.

---------------------------------------------------------------------------------------------------------------------
Estabilidade do clusters
para verificar se o clusters esta Estavel podemos dividir os dados em partes e ver como esta a validação do cluster em cada conjunto de dados.
