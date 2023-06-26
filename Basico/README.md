[[https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
# Índice
* [Tipos De Variaveis](#tipos-de-variaveis)
* [Operadores Logica](#operadores-logica)
* [Operadores Condicional](#operadores-condicional)
* [Laço de repetição for](#laço-de-repetição-for)
* [Laço de repetição while](#laço-de-repetição-while)
* [Manipulação de String](#manipulação-de-string)
* [Estrutura de Dados](#estrutura-de-dados)
* [Varedura de Dados](#varedura-de-dados)


# Tipos De Variaveis
 ## **[Inteiro](#int)**

    
O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ser positivo ou negativo.
Por exemplo, -20, 4, 5, 10 são números inteiros, enquanto 3.17, 1/5, 2.9 não são
   
   
**Exemplo:**
```py 
idade = 18
ano = 2002

print(type(idade))
print(type(ano))
```

**Saida:**
```py 
<class 'int'>
<class 'int'>
```

## **[Ponto Flutuante ou Decimal](#float)**
    
É um tipo composto por caracteres numéricos (algarismo) decimais.
O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.


**Exemplo:**
```py
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))
```
**Saida:**
```py
<class 'float'>
<class 'float'>
```



## **[Tipo Complexo](#complex)**
    
Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
Esse tipo normalmente é usado em cálculos geométricos e científicos.
Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo.
   
**Exemplos:**
```py
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))
```

**Saida:**
```py
<class 'complex'>
<class 'complex'>
(2+5j)
```

## **[String](#str)**
    
É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
    
**Exemplos:**

```py
nome = 'Guilherme'
profissao = 'Engenheiro de Software'

print(type(profissao))
print(type(nome))
```
**Saida:**
```py
<class 'str'>
<class 'str'>
```    

## **[Boolean](#bool)**
Tipo de dado lógico que pode assumir apenas dois valores: False ou True.

**Exemplo:**

```py
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))
```
**Saida:**
```py
<class 'bool'>
<class 'bool'>
```

## **[List](#list)**

Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.
Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos

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




* [Tuple](#tuple)

* [Dictionary](#dic)




## Operadores Logica




## Operadores Condicional





## Laço de repetição for





## Laço de repetição while





## Manipulação de String





## Estrutura de Dados





## Varedura de Dados
](https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
# Índice
* [Tipos De Variaveis](#tipos-de-variaveis)
* [Operadores Logica](#operadores-logica)
* [Operadores Condicional](#operadores-condicional)
* [Laço de repetição for](#laço-de-repetição-for)
* [Laço de repetição while](#laço-de-repetição-while)
* [Manipulação de String](#manipulação-de-string)
* [Estrutura de Dados](#estrutura-de-dados)
* [Varedura de Dados](#varedura-de-dados)


# Tipos De Variaveis
 ## **[Inteiro](#int)**

    
O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ser positivo ou negativo.
Por exemplo, -20, 4, 5, 10 são números inteiros, enquanto 3.17, 1/5, 2.9 não são
   
   
**Exemplo:**
```py 
idade = 18
ano = 2002

print(type(idade))
print(type(ano))
```

**Saida:**
```py 
<class 'int'>
<class 'int'>
```

## **[Ponto Flutuante ou Decimal](#float)**
    
É um tipo composto por caracteres numéricos (algarismo) decimais.
O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.


**Exemplo:**
```py
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))
```
**Saida:**
```py
<class 'float'>
<class 'float'>
```



## **[Tipo Complexo](#complex)**
    
Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
Esse tipo normalmente é usado em cálculos geométricos e científicos.
Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo.
   
**Exemplos:**
```py
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))
```

**Saida:**
```py
<class 'complex'>
<class 'complex'>
(2+5j)
```

## **[String](#str)**
    
É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
    
**Exemplos:**

```py
nome = 'Guilherme'
profissao = 'Engenheiro de Software'

print(type(profissao))
print(type(nome))
```
**Saida:**
```py
<class 'str'>
<class 'str'>
```    

## **[Boolean](#bool)**
Tipo de dado lógico que pode assumir apenas dois valores: False ou True.

**Exemplo:**

```py
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))
```
**Saida:**
```py
<class 'bool'>
<class 'bool'>
```

## **[List](#list)**
https://pythonacademy.com.br/blog/listas-no-python

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
```py
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








* [Tuple](#tuple)

* [Dictionary](#dic)




## Operadores Logica




## Operadores Condicional





## Laço de repetição for





## Laço de repetição while





## Manipulação de String





## Estrutura de Dados





## Varedura de Dados
)https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
# Índice
* [Tipos De Variaveis](#tipos-de-variaveis)
* [Operadores Logica](#operadores-logica)
* [Operadores Condicional](#operadores-condicional)
* [Laço de repetição for](#laço-de-repetição-for)
* [Laço de repetição while](#laço-de-repetição-while)
* [Manipulação de String](#manipulação-de-string)
* [Estrutura de Dados](#estrutura-de-dados)
* [Varedura de Dados](#varedura-de-dados)


# Tipos De Variaveis
 ## **[Inteiro](#int)**

    
O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ser positivo ou negativo.
Por exemplo, -20, 4, 5, 10 são números inteiros, enquanto 3.17, 1/5, 2.9 não são
   
   
**Exemplo:**
```py 
idade = 18
ano = 2002

print(type(idade))
print(type(ano))
```

**Saida:**
```py 
<class 'int'>
<class 'int'>
```

## **[Ponto Flutuante ou Decimal](#float)**
    
É um tipo composto por caracteres numéricos (algarismo) decimais.
O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.


**Exemplo:**
```py
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))
```
**Saida:**
```py
<class 'float'>
<class 'float'>
```



## **[Tipo Complexo](#complex)**
    
Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
Esse tipo normalmente é usado em cálculos geométricos e científicos.
Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo.
   
**Exemplos:**
```py
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))
```

**Saida:**
```py
<class 'complex'>
<class 'complex'>
(2+5j)
```

## **[String](#str)**
    
É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
    
**Exemplos:**

```py
nome = 'Guilherme'
profissao = 'Engenheiro de Software'

print(type(profissao))
print(type(nome))
```
**Saida:**
```py
<class 'str'>
<class 'str'>
```    

## **[Boolean](#bool)**
Tipo de dado lógico que pode assumir apenas dois valores: False ou True.

**Exemplo:**

```py
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))
```
**Saida:**
```py
<class 'bool'>
<class 'bool'>
```

## **[List](#list)**
https://pythonacademy.com.br/blog/listas-no-python

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
```py
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








* [Tuple](#tuple)

* [Dictionary](#dic)




## Operadores Logica




## Operadores Condicional





## Laço de repetição for





## Laço de repetição while





## Manipulação de String





## Estrutura de Dados





## Varedura de Dados
](https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
# Índice
* [Tipos De Variaveis](#tipos-de-variaveis)
* [Operadores Logica](#operadores-logica)
* [Operadores Condicional](#operadores-condicional)
* [Laço de repetição for](#laço-de-repetição-for)
* [Laço de repetição while](#laço-de-repetição-while)
* [Manipulação de String](#manipulação-de-string)
* [Estrutura de Dados](#estrutura-de-dados)
* [Varedura de Dados](#varedura-de-dados)


# Tipos De Variaveis
 ## **[Inteiro](#int)**

    
O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ser positivo ou negativo.
Por exemplo, -20, 4, 5, 10 são números inteiros, enquanto 3.17, 1/5, 2.9 não são
   
   
**Exemplo:**
```py 
idade = 18
ano = 2002

print(type(idade))
print(type(ano))
```

**Saida:**
```py 
<class 'int'>
<class 'int'>
```

## **[Ponto Flutuante ou Decimal](#float)**
    
É um tipo composto por caracteres numéricos (algarismo) decimais.
O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.


**Exemplo:**
```py
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))
```
**Saida:**
```py
<class 'float'>
<class 'float'>
```



## **[Tipo Complexo](#complex)**
    
Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
Esse tipo normalmente é usado em cálculos geométricos e científicos.
Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo.
   
**Exemplos:**
```py
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))
```

**Saida:**
```py
<class 'complex'>
<class 'complex'>
(2+5j)
```

## **[String](#str)**
    
É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
    
**Exemplos:**

```py
nome = 'Guilherme'
profissao = 'Engenheiro de Software'

print(type(profissao))
print(type(nome))
```
**Saida:**
```py
<class 'str'>
<class 'str'>
```    

## **[Boolean](#bool)**
Tipo de dado lógico que pode assumir apenas dois valores: False ou True.

**Exemplo:**

```py
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))
```
**Saida:**
```py
<class 'bool'>
<class 'bool'>
```

## **[List](#list)**
https://pythonacademy.com.br/blog/listas-no-python

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
```py
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








* [Tuple](#tuple)

* [Dictionary](#dic)




## Operadores Logica




## Operadores Condicional





## Laço de repetição for





## Laço de repetição while





## Manipulação de String





## Estrutura de Dados





## Varedura de Dados
)https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
# Índice
* [Tipos De Variaveis](#tipos-de-variaveis)
* [Operadores Logica](#operadores-logica)
* [Operadores Condicional](#operadores-condicional)
* [Laço de repetição for](#laço-de-repetição-for)
* [Laço de repetição while](#laço-de-repetição-while)
* [Manipulação de String](#manipulação-de-string)
* [Estrutura de Dados](#estrutura-de-dados)
* [Varedura de Dados](#varedura-de-dados)


# Tipos De Variaveis
 ## **[Inteiro](#int)**

    
O tipo inteiro é um tipo composto por caracteres numéricos (algarismos) inteiros.
É um tipo usado para um número que pode ser escrito sem um componente decimal, podendo ser positivo ou negativo.
Por exemplo, -20, 4, 5, 10 são números inteiros, enquanto 3.17, 1/5, 2.9 não são
   
   
**Exemplo:**
```py 
idade = 18
ano = 2002

print(type(idade))
print(type(ano))
```

**Saida:**
```py 
<class 'int'>
<class 'int'>
```

## **[Ponto Flutuante ou Decimal](#float)**
    
É um tipo composto por caracteres numéricos (algarismo) decimais.
O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.


**Exemplo:**
```py
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))
```
**Saida:**
```py
<class 'float'>
<class 'float'>
```



## **[Tipo Complexo](#complex)**
    
Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
Esse tipo normalmente é usado em cálculos geométricos e científicos.
Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
A função complex(real[, imag]) do Python possibilita a criação de números imaginários passando como argumento: real, que é a parte Real do número complexo e o argumento opcional imag, representando a parte imaginária do número complexo.
   
**Exemplos:**
```py
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))
```

**Saida:**
```py
<class 'complex'>
<class 'complex'>
(2+5j)
```

## **[String](#str)**
    
É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
    
**Exemplos:**

```py
nome = 'Guilherme'
profissao = 'Engenheiro de Software'

print(type(profissao))
print(type(nome))
```
**Saida:**
```py
<class 'str'>
<class 'str'>
```    

## **[Boolean](#bool)**
Tipo de dado lógico que pode assumir apenas dois valores: False ou True.

**Exemplo:**

```py
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))
```
**Saida:**
```py
<class 'bool'>
<class 'bool'>
```

## **[List](#list)**
https://pythonacademy.com.br/blog/listas-no-python

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
```py
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








* [Tuple](#tuple)

* [Dictionary](#dic)




## Operadores Logica




## Operadores Condicional





## Laço de repetição for





## Laço de repetição while





## Manipulação de String





## Estrutura de Dados





## Varedura de Dados
