Pandas:

o pandas utiliza basicamente o tipo DataFrame e o tipo Series.
deve existir um tratamento das  informaçãoes para que os dados entrem no dataframe no formato correto.
por exemplo, ao exportar os dados do banco de dados as colunas do banco ficam em uma lista separada apenas por virgula uma coluna da outra.
precisamos que as listas dentro da lista geral seja extraidas e reorganizadas

0
0	[AMC_BAC01.comando, 0.0, 192]
1	[AMC_BAC01.estado, 0.0, 192]
2	[AMC_BAC01.falha, 0.0, 192]
3	[AMC_BAC02.comando, 0.0, 192]

[
	[AMC_BAC01.comando, 0.0, 192]
	[AMC_BAC01.estado, 0.0, 192]
	[AMC_BAC01.falha, 0.0, 192]
	[AMC_BAC02.comando, 0.0, 192]
]

no exemplo acima existe varias filas dentro de outra fila pai.
essa lista dentro de lista deve ser convertido em dicionario para que os primeiros atributos sejam organizadas em uma coluna, simulando uma tabela.
para isso vamos criar um dicionario e adicionar os itens da lista a esse dicionario.

    dict_list = []# criação da lista
    for row in data: #aqui vai ser varrido os items da lista, so que como falamos antes é uma lista com outra dentro logo row vai ter o valor: [AMC_BAC01.comando, 0.0, 192] da linha 0 e depois vai ter os valores da linha1 e etc.
        dict_list.append({ #sabendo que vamos varrer listas vamos adicionar vamos transformar a lista de dentro em um dicionario e a lista pai vai continuar existindo, a estrutura dos dados vai ser uma lista pai e varios dicionarios filhos, assim o pandas entende
            'tagname': row[0],
            'valor': row[1],
            'qualidade': row[2]
        })# aqui estamos adicionando em uma lista um dicionario por linha e esses dicionarios teram 3 items e cada um com seu values. com isso conseguimos realizar os analises nescessario por values ou por itens.

    # Criando o DataFrame a partir da lista de dicionários
    df = pd.DataFrame(dict_list)# o dataframe precisa ter a estrutura de tabela, isso é um fundamento principal.


df['valor'] = df['valor'].round(2)# esse codigo condiciona os valores da coluna 'valor' a mostrarem apenas 2 casas decimais
df = df.to_html(index=False)# a primeira coisa que devemos fazer apos conseguir puxar os dados é organizar ele em tabela, o index igual a false faz com que a coluna de indice nao apareca mais  somente apos a tabela esta bem formatada é que vamos modificar os dados em visoes diferentes.
df.reset_index(drop=True, inplace=True)# em uma situação de filtros onde usariamos o indice fazemos assim para recetar a contagem como se fosse uma tabela nova.
df = df[['tagname', 'valor']]# ja aqui selecionamos as colunas na qual queremos trabalhar
--------------------------------------------------------------
df_off = df_off['tagname'].str.split('_').str[0].value_counts().reset_index()# esse cara cria uma coluna nova chamada filtro e separa a coluna tagname em duas parte, uma antes do '_' e outra depois. quando colocamos str[0] pegamos a primeira parte
df = df['tagname'].str.split('_').str[0].value_counts()# nesse codigo df deixe de ser um DataFrame e se torna uma Serie, a tecnica pra transformalo novamente em Dataframe é a seguinte:reset_index() transforma o resultado em um novo DataFrame, onde os prefixos são a nova coluna 'index' (o índice padrão do DataFrame) . uma serie é uma tabela com um indici e uma coluna ja um dataframe é uma tabela com um indici e varias colunas. precisamos converter o tipo series em dataframe no nosso exemplo pq a pagina html ja esta estruturada pra receber uma tabela value_counts() em uma coluna de um DataFrame no Pandas, o resultado é uma Series onde os índices são os valores únicos da coluna e os valores são as contagens de cada valor na coluna.
df.columns = ['Nome', 'Contagem'] por ultimo colocamos nomes no antigo indice que virou coluna e na outra coluna

---------------------------------------------------------------------------------------

```
duplicated = df[df.duplicated('TagName', keep='first')]
```

no caso acima o metodo duplicated so identifica os valores duplicados em df e joga para a variavel duplicated

```

```