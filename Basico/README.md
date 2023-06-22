https://pythonacademy.com.br/blog/tipos-de-variaveis-no-python
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
