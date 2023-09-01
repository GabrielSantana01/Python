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