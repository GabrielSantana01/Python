No machine learn somos apresentado a algumas palavras chaves que devemos saber oque é:

features =  é a quantidade de caracteristicas que temos(coluna)

itens = são todas as linhas dos dados

treino = A ideia no algoritmo de machine learn é estimar as classes de nosso dados. ou seja quando temos amostras de dados
pegamos parte dessa amostra para treinar o script.No caso desse aprendizado  supervisionado  utilizamos as features
existente para estipular a qual classe cada item pertence.

teste = Ainda assim para conseguirmos estimar precisamos tambem realizar o teste. que consiste em pegar uma parte dos dados que
não foi usado no treino, e fazemos o algoritmo de machine learn estipular qual vai ser a classe de cada item, atraves do 
que ja foi aprendido na etapa de treino. ou ate mesmo podemos criar features novas para testarmos a classificação obtida pelo nosso modelo de ML.

taxa de acerto = para sabermos a estimativa do quanto o algoritmo de machine learn acertou na etapa de teste temos que 
primeiramente salvar a classificação verdadeira da amostra de teste, para compararmos com a classificação realizada pelo
algoritmo.

classes/label(etiqueta) = é a classificação dos itens... para sabermos a qual categoria o item pertence.
no nosso projeto temos que identificar todos os topicos acima para entregar resultados.O python tem uma biblioteca
chamada sklearn.
