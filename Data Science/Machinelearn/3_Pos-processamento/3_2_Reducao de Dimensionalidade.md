deixei o nome do arquivo como Reducao de Dimensionalidade mas poderia ser entendendo os valores dos atributos.

para diminuir a dimensão de um dataframe para a criação de um modelo e ter melhoria nesse modelo ja que com essa 
redução teremos menos dados para alcançar o mesmo resultado, e mesma qualidade do modelo, é nescessario entender
quais features tem maior relevancia no modelo aplicado, quais features tem maiores correlações entre si.

em um caso de agrupamento por exemplo, se temos 5 agrupamentos, o quais features impactaram mais para determinar que 
um item pertece a um agrupamento e não a outro, para sabermos disso temos que usar tecnicas de estatistica, e ver 
as particularidades das relações das features atraves dos valores estatisticos.

essa é uma medida tomada quando temos muitas features e ao visualiza-las corelação por corelação nao conseguimos chegar
a conclusões. ja utilizando dados estatisticos conseguimos perceber comportamentos mais claramente quando temos muitos dados.

entao temos a analise com visualização, estatistica e variancia

a ideia de realizar um analise usando a variancia dos clusters server para metricas de validação interna onde utilizamos
o atributo .cluster_centers_ para um modelo de agrupamento. esse atributo vai nos trazer uma lista com um unico valor
para cada features que corresponde a variancia que ocorre nessa features agrupada é claro em seu devido cluster.
tipo a features 1 para o cluster 1 vai ter um valor na sua variancia e se essa essa features impactar no modelo Euclidiana
tera um valor bem diferente no cluster 2. com isso sabemos a unfluencia das fetures no modelo.