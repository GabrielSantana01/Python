para verificar se nosso dados estão desbalanceado vamos criar um grafico de barra com os valores da classe em questão


import seaborn as sns
%matplotlib inline

ax = sns.countplot(x='Churn', data=dados_final)

usando o codigo acima teremos a contagem da coluna Churn dos dados dados_final

identificado o desbalanceamento dos dados da nossa classe, agora vamos aplicar uma tecnica chamada Oversampling para balancear os dados

uma das tecnicas de oversampling é a SMOTE :
Consiste em realizar a criação de novas observações da classe quando há menos amostras, tendo como objetivo igualar a proporção entre as categorias.
Uma das técnicas de oversampling muito utilizada é a SMOTE. Sua ideia consiste em criar observações intermediárias entre os dados que estão próximos. Por exemplo, se minutos totais por dia são 129.1 e 146.3, então será criada uma amostra com os minutos totais por dia com 137.7. Lembrando que não é necessariamente a média entre as amostras.

Primeiro instalamos a biblioteca
--------------------------------------------------------------------------------------
!pip install -U imbalanced-learn


lembrando que os dados devem ja esta preprocessados
---------------------------------------------------------------------------------------
import pandas as pd
url = 'Customer-Churn.csv'
dados = pd.read_csv(url, sep=',')
X = dados.drop('Churn', axis = 1)
y = dados['Churn']
traducao_dic = {'Sim' : 1, 'Nao': 0}
dadosmodificados = dados [['Conjuge', 'Dependentes', 'TelefoneFixo', 'PagamentoOnline', 'Churn']].replace(traducao_dic)
dummie_dados = pd.get_dummies(dados.drop(['Conjuge', 'Dependentes', 'TelefoneFixo', 'PagamentoOnline', 'Churn'], axis=1))
dados_final = pd.concat([dadosmodificados, dummie_dados], axis=1)
dados_final.head()


ai usaremos o SMOTE nos dados_Final separando as Features da classe(Churn)
-----------------------------------------------------------------------------------------
#abaixo é definido X e Y
X = dados_final.drop('Churn', axis = 1)
y = dados_final['Churn']

importamos a biblioteca e instanciamos um objeto smt do tipo SMOTE() e colocamos as Features e classe no objeto smt executando o metodo fit_resample()
------------------------------------------------------------------------------------------
from imblearn.over_sampling import SMOTE

smt = SMOTE(random_state=42)  # Instancia um objeto da classe SMOTE com um numero random setado 
X, y = smt.fit_resample(X, y)  # Realiza a reamostragem do conjunto de dados


ai rodamos novamente o grafico e vemos que o SMOTE deixou a mesma contidade de amostragem tanto Churn sim e de Churn não.
------------------------------------------------------------------------------------------
ax = sns.countplot(x='Churn', data=dados_final)  # plotando a variável target balanceada.