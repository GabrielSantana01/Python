
Modelo  Bernoulli Naive Bayes
principio da indepetencia condicional = teorema de Bayes(baize)
teorema de bernoulli naive bayes(bernuli naive beize) = cada uma das features contribuem de forma idepedente entre si, para determinar a classe.
 
  A Verossimilhança mede a probabilidade de uma determinada característica acontecer, sendo que a classe aconteceu
a probabilidade de X dado que Y aconteceu, também conhecida como Verossimilhança.OBS: ao verificarmos a probabilidade do valor de uma features ocorre atraves do resultado da classe desse item.

tendo a formula: P(y/x) = P(X/y) * P(y)/P(X) , vemos que identificar como ler essa primeira parte:P(X/y): qual a probabilidade de acontecer x dado que Y ocorreu.
OBS: na formula x são as features e Y a classe.

probabilidade a priori da classe: Quando temos a pobabilidade x ja que y ocorreu temos agora que multiplicar pela probabilidade de Y:
essa prioridade de Y mostra a probabilidade da classe ocorrer em todos o conjunto de amostra.ou seja é a prevalência daquela classe sobre toda a amostra


ja a probabilidade a priori da evidência é a probabilidade de X ocorrer.Isso quer dizer que queremos agora saber a prevalência dessa característica sobre a amostra. 
Qual a probabilidade de não se ter dependentes em toda a nossa base de clientes.

probabilidade a posteriori =  a probabilidade de uma determinada classe ocorrer sendo que um conjunto de características ocorreu. 
Qual a probabilidade da Maria ser classificada com um Churn igual a não, sendo que ela não tem dependentes.

Qual a probabilidade dela ter um Churn igual a não? É isso que o Teorema de Bayes calcula.


agora falando do modelo Bernoulli Naive Bayes
Multinomial de Bernoulli = é tipo de distribuição em que os dados estão apenas em variáveis binárias.
dada a formula = p(xi\y) = P(i\y)xi + (1-p(i\y))(1-xi)

na primeira operação começamos pela probabilidade de i dado que y aconteceu P(i\y)xi temos a identificação do parâmetro P da distribuição de Bernoulli: 
lembrando que esse i pode ser um valor infinito de 1 até N, e o i é o número de características do nosso conjunto de variáveis no exemplo da maria tinhamos 38 is.

Xi que já é um velho conhecido, que é o conjunto de características