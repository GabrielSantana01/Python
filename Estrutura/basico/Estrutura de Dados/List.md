Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.
Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos
Uma Lista (list) em Python, nada mais é que uma coleção ordenada de valores, separados por vírgula e dentro de colchetes []. Elas são utilizadas para armazenar diversos itens em uma única variável
**Exemplo:**
```py
alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0] 

print(type(alunos))
print(type(notas))
```
**Saida:**

```py
<class 'list'>
<class 'list'>
```
## **Criando listas**

Existem várias maneiras de se criar uma lista.
A maneira mais simples é colocar os elementos da lista em colchetes, por exemplo:

```py
# Lista com apenas um elemento
lista = ["PythonAcademy"] 
```
Também podemos criar uma lista vazia:

```py
lista = [] 
```
Para criar uma lista com diversos itens, podemos fazer:
```py
lista = ['Python', 'Academy', 2021] 
```
Também podemos utilizar a função list do próprio Python (built-in function):
```py
lista = list(["Python Academy"]) 
```
Outra forma é criar listas resultantes de uma operação de List Comprehensions!
```py
[item for item in iteravel]
```
Podemos ainda criar listas através da função range(), dessa forma:
```py
list(range(10))
```
Saida:
```py## CONCEITO
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
### Acessando dados da lista
Todos os itens de uma lista são indexados, ou seja para cada item da lista um índice é atribuído da seguinte forma: lista[indice].
Exemplo com itens:
```py
[frutas = ['Maça', 'Banana', 'Jaca', 'Melão', 'Abacaxi']]
```
E assim ficaria a sequência de índices:
![Basico/img/lista01.png](https://github.com/GabrielSantana01/Python/blob/main/Basico/img/lista01.png)

Em Python os índices são iniciados em 0.Ou seja, como podemos acessar o primeiro item da lista que é o índice 0? Veja abaixo:
```py
print(frutas[0])
```
A saída como previsível foi a string com a palavra Maça por ocupar o índice 0:

```py
Maça
```
### Indexação negativa
E se o desejado for o último item?
Neste momento entramos no conceito de indexação negativa, que significa começar do fim. -1 irá se referir ao último item. Por exemplo:
![Basico/img/lista02.png](https://github.com/GabrielSantana01/Python/blob/main/Basico/img/lista02.png)
Dessa forma, para buscar pelo último item da lista:
```py
print(frutas[-1])
```
Saida: 
```py
Abacaxi
```
### Lista dentro de lista
Suponha que exista uma lista dentro de uma lista, assim:
```py
lista = ['item1', ['python', 'Academy'], 'item3']
```
Como podemos acessar o primeiro índice do item que é uma lista?
A resposta é simples, basta selecionar a posição em que se localiza a lista para ter acesso a ela, assim:
```py
sublista = lista[1]
print(sublista[0])
```
Ou ainda:
```py
print(lista[1][0])
```
Ambos obtém mesmo resultado:
```py
'python'
```
### Fatiando uma lista (slicing)
O fatiamento de listas, do inglês slicing, é a extração de um conjunto de elementos contidos numa lista. Ele é feito da seguinte forma:
```py
lista[ inicio : fim : passo ]
``` 
### Explicando cada elemento:

* *início* se refere ao índice de início do fatiamento.
* *fim* se refere ao índice final do fatiamento. A lista final não vai conter esse elemento.
* *passo* é um parâmetro opcional e é utilizado para se pular elementos da lista original

Se quisermos criar uma fatia de uma lista do índice 2 ao 4, podemos fazer da seguinte forma:
```py
lista = [10, 20, 30, 40, 50, 60]
print(lista[2:5])
``` 
O slicing conta a partir do índice 2 até o índice 5 (mas não o utiliza), pegando os índices 2, 3, 4.
Sua saída será:
```py
[30, 40, 50]
``` 
### Percorrendo listas
A forma mais comum de percorrer os elementos em uma lista é com um loop for elemento in lista, assim:
```py
lista = [10, 20, 30, 40, 50, 60]
for num in lista:
    print(num)
```
Saida:
```py
10
20
30
40
50
60
```
Com a função enumerate() podemos percorrer também o índice referente a cada valor da lista:
```py
lista = [10, 20, 30, 40, 50, 60]
for indice, valor in enumerate(lista):
    print(f'índice={indice}, valor={valor}')
```
Saida:
```py
índice=0, valor=10
índice=1, valor=20
índice=2, valor=30
índice=3, valor=40
índice=4, valor=50
índice=5, valor=60
```
Que tal poupar algumas linhas e obter o mesmo resultado com List Comprehension?
```py
[print(num) for num in lista]

# Com enumerate:
[print(f'índice={indice}, valor={valor}') for indice, valor in enumerate(lista)]
```
A saída será a mesma! 

Eu vou usar links apartir de agora, como biblioteca. a ideia é acessar essas bibliotecas toda vez que quiser usar uma função em especifico. 
A organização agora tem que categorizar essa biblioteca.

https://pythonacademy.com.br/blog/manipulacao-de-listas-no-python


uma outra estrutura de lista é o Conjunto (ou set) nesse não é possivel repetir valores
por exemplo em uma lista é possivel ter os valores abaixo:
```py
const lista = [1, 1, 1, 3, 5, 7, 9];
```py

como no conjunto isso não é possivel:
```py
lista = [1, 1, 1, 3, 5, 7, 9];
conjunto = Set(lista);
print(conjunto);
# Set(5) { 1, 3, 5, 7, 9 }
```py