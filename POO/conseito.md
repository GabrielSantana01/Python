#quando precisamos acessar atributos de uma classe em uma outra classe precisamos realizar uma importação. ex: from modulo import classe.
#porem criamos metodos para que não rode todo o conteudo da classe importada.

para criarmos uma classe usamos a seguinte sentença dentro do modulo(arquivo com o ponto .py): class MinhaClasse:
e dentro da classe com a devida identação criamos o metodo construtor que é um metodo que tera todos os atributos da classe:

```python
 def __init__(self, atributo01, atributo02):
   self.atributo01 = atributo01
   self.atributo02 = atributo02
   ```

para que esses atributos não sejam acessados diretamente, deixamos esses atributos como privados usando o (_) duas vezes antes do atributo. logo teremos:
```python 
def __init__(self, atributo01, atributo02):
   self.__atributo01 = atributo01
   self.__atributo02 = atributo02
```
*OBS: com isso temos que criar metodos qualquer ou um metodo set e get para conseguir ler e escrever no atributo privado.

------------------------------------------------------------------------------------------------------------------------
quando instanciamos a classe atraves da criação de um objeto podemos acessar o contrutor diretamente colocando os atributos na chamada da classe:
```python
objeto01 = MinhaClasse(atributo01, atributo02)
print(objeto01.atributo01)
print(objeto01.atributo02)
```
#porem com isso ao chamar o arquivo python em outro arquivo ele passa a chamar a função automaticamente por isso que criamos um 
```python
if (__name__ == '__main__'):
  def função_Do_Arquivo_Python():
```
#a interpretação para o if acima é de uma pergunta. se o arquivo rodado(__name__) é o principal(__main__). caso seja o principal ele roda oq esta dentro do if, caso não, não faz nada, com isso quando rodarmos um arquivo python diretamente 
#a função onde esta contido o codigo sera rodada. e quando rodamos esse arquivo atraves de outro o metodo que contem o codigo sera rodado somente quando chamado.


a classe, pois com ela o arquivo python so vai rodar o codigo do metodo quando a classe for estanciada e o metodo chamado.'''

----------------------------------------------------------------------------------------------------------------------
quando criamos uma variavel dentro de um metodo em uma classe não conseguimos acessar essa variavel por outro metodo
pois essa é uma variavel local. para acessarmos uma variavel em todos os metodos da classe temos que criar essa variavel
no metodo construtor da classe: __init__, ou seja temos que criar uma variavel global da classe.

if (__name__ == '__main__'): # essa verificação valida se o script que estamos rodando é o principal do programa caso seja vai existir um metodo main() dentro da class e o interpretador python  ai rodar primeiramente o metodo main() quando a classe for chamada.

ai dentro de main() vamos chamar todos os passos que queremos executar em nosso programa.
-----------------------------------------------------------------------------------------------------------
existe uma função dir que mostra todos os metodos de sistema de uma classe
e existe tambem a função vars que mostra todas as funções e atributos de uma classe

o metodo de sistema __init__ server para ser o construtor da classe
o metodo __str__ server para exibir os atributos da classe como string
OBS: quando criamos uma classe somente com __init__ e com qualquer outro metodo comum, todos os metodos vao ser chamado dessa classe quando chamamos a classe na instanciação... por isso que criamos a estrutura main.