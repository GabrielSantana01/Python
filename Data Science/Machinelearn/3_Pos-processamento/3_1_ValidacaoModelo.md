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

para verificar o coeficiente de silhouette 
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
existe outra metrica baseada em validação interna chamada de Davies-Bouldin

sua compactação calcula a distancia dos elementos para o centro do cluster. e cria uma media para essas distancia.

fórmula abaixo é utilizada para medir a similaridade entre dois clusters i e j. Quanto menor o valor final mais similares são os clusters.
Desse modo, sabemos que s mede a compactação dos clusters e d mede a separação entre eles.

Rij = (Si + Sj)/Dij
---------------------------------------------------------------------------------------------------------------------------------------------
indice Calinski-Harabasz

tr(Bk) = dispersão entre do (Between)clusters
tr(Wk) = dispersão dentro (within)clusters
k = numero de clusters 
Ne = numeros de elementos do clusters

s = ((tr(Bk)/tr(Wk)) x ((Ne-k)/(k-1)))
