
#Criar lista
frutas = list()
-------------------------------------------------------

SINTAX = frutas = ['maça', 'banana', 'morango', 'manga']
a lista é mais lenta
-------------------------------------------------------
add item na lista=
frutas.append('abacaxi')# vai pro final da lista
frutas.insert(2,'laranja')
print('fruta')
frutas = ['maça', 'banana','laranja','morango', 'manga']
frutas.append(input('insira uma fruta'))
-------------------------------------------------------
alterar valor de uma possição=
frutas[2] = 'laranja'

-------------------------------------------------------
excluir item na lista=

del frutas[2] # remover pelo indice
frutas.pop(2) # tb remover pelo indice
frutas.remove('laranja') # remove pelo valor

-------------------------------------------------------
ORDERNAR LISTA=
frutas.sort()# o metodo provavelmente so numeros, esse metodo altera a lista original
copia = frutas# o igual cria uma ligação entra as duas listas e os dois vao receber a alteração

para criar uma copia é preciso fazer o seguinte:

copia = frutas[:]# copia recebe todos os itens de frutas sem criar uma ligação entre as listas.
ou usar a função sorted é uma billtind do python,  cria uma copia da lista

-------------------------------------------------------
-------------------------------------------------------
                                            TUPLA = 

SINTAX = frutas = (maça, banana, morango, manga)

A tupla é imutavel


-------------------------------------------------------
-------------------------------------------------------

Para pecorrer item a item de um dicionario usamos o for

dados = {
    'Crossfox': {'km': 35000, 'ano': 2005}, 
    'DS5': {'km': 17000, 'ano': 2015}, 
    'Fusca': {'km': 130000, 'ano': 1979}, 
    'Jetta': {'km': 56000, 'ano': 2011}, 
    'Passat': {'km': 62000, 'ano': 1999}
}

ef km_media(dataset, ano_atual):
   for item in dataset.values():
        result = item['km'] / (ano_atual - item['ano'])
        print(result)
km_media(dados, 2019)

no exemplo acima é acessado os itens 'km' e os itens 'ano' do dicionario
