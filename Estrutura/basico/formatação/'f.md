'''para formatar os valores podemos usar a função .format ou o editor de string f''

USANDO O .format = 
  print('{}'.format()) - oque estiver sendo verificado dentro da função format estara dentro das chaves que esta dentro das aspas simples.
  
 nome = input('Insira seu nome')
idade = input('insira sua idade')
print('Ola {} parabens pelos seus {} anos'.format(nome, idade))

pode-se usar indice tb. onde o format começa a contar do 0 caso chamemos o indice 1 primeiro, os valores serao exibidos na ordem solicitada.
print('Ola {1} parabens pelos seus {0} anos'.format(nome, idade))
 


OU 

print('Ola {nome} parabens pelos seus {idade} anos'.format(nome ='Gabriel', idade = 32))


USANDO f'' = 

print(f'ola {nome} tudo bem com vc ? parabens pelos seus {idade} anos)

'''
Formatando valores = 

'''
:s - formatar string
:d - formatar int
:f - formatar float
:.(numero)f - quantidade de casa decimais
:(caracter) (< OU > OU ^) (quantidade de repetição)(tipo s ou d ou f) - essa sentença repete o caracter uma determinada quantidade de vezes.
f'o numero inserido foi{idade:@>5.2f}'
print('_'* len(forca))# exibi a quantidade de _ no tamanho de forca
'''
\t # concatena os valores
print(f'o nome{} foi aprovado com nota{}', end='') # o end no final é para exibir os valores na mesma linha
-----------------------------------------------------------------------------------------------------
https://www.python.org/doc/
https://wiki.python.org.br/EstruturaSequencial
https://docs.python.org/pt-br/3/library/string.html#grammar-token-format-string-format_spec
https://cienciaprogramada.com.br/2022/03/formatacao-strings-python/
