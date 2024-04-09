print('Hi {} tudo bem? me chamo {}'.format('Gabriel', 'Carla'))


print('Hi {} tudo bem? me chamo {} corro 2f'.format('Gabriel', 'Carla'))

nome_aluno = 'Fabricio Daniel'

print('Nome do aluno: {}'.format(nome_aluno))


nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno, media_aluno))
print('Nome do aluno é {}, ele tem {} anos e sua média é {}.'.format(nome_aluno, idade_aluno, media_aluno))

print("Estudar é um esforço constante,\nÉ como cultivar uma planta,\nPrecisamos de dedicação e paciência,\nPara ver o fruto amadurecer.")
print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')
print("Caminho do arquivo: C:\\arquivos\\documento.csv")
print("Ouvi uma vez \"Os frutos do conhecimento são os mais doces e duradouros de todos.\"")
print('Minha professora uma vez disse \'Estudar é a chave do sucesso.\' ')

'''
@>: Isso indica que o valor deve ser alinhado à direita (>), 
e o caractere @ indica o tipo de preenchimento, que neste caso é um espaço em branco.
5.2f: Isso especifica o formato do número de ponto flutuante.
5 indica o número total de caracteres que a string deve ter, incluindo o ponto decimal e os dígitos.
.2 especifica que dois desses caracteres são reservados para os dígitos após o ponto decimal.
f indica que é um número de ponto flutuante.
''' 
print(f'o numero inserido foi: {idade_aluno:@>5.2f}')

from datetime import datetime

hoje = datetime.now()
print(f"Data: {hoje:%d/%m/%Y}, Horário: {hoje:%H:%M}")


margem_lucro = 0.27
print(f"Margem: {margem_lucro:.1%}")
#-----------------------------------------------------------------------
# pro estilo que prefiro, essa é a configuração correta.
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
#-----------------------------------------------------------------------
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

print("teste: {:.2f}; {:-f}".format(3.14, -3.14))

help(round)

