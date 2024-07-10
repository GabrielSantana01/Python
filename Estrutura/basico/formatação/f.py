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

round(variavel, 1) # o resultado tem 1 casa decimal

#List Comprehensions
valor_int = sum(tabela._coluna1 for interacao in self.tabela) 
# no codigo acima estamos somando  os valores das linha existente em uma coluna de uma tabela.
nomes = ["Ana", "Maria", "Pedro", "João", "Marta"]
nomes_com_m = [nome for nome in nomes if nome.startswith("M")]
print(nomes_com_m)
#-----------------------------------------------------------------------------
dicionario = {'a': 1, 'b': 2, 'c': 3}
chaves = [chave for chave in dicionario]
print(chaves)
#------------------------------------------------------------------------------
lista_de_listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
achatar = [item for sublista in lista_de_listas for item in sublista]
print(achatar)
#-------------------------------------------------------------------------------
matriz = [[j for j in range(3)] for i in range(3)]
print(matriz)

#----------------------------------------------------------------------------
'''
text = "Python"
print(text.ljust(10))  # "Python    " o metodo ljust faz a string ter 10 caracteres
'''
#---------------------------------------------------------------------------------
'''
@property em Python é usado para criar métodos que podem ser acessados como atributos
, sem a necessidade de parênteses. Isso é útil para encapsular o acesso a atributos privados de uma classe, permitindo o controle sobre como esses atributos são acessados e modificados.
'''

class Produto:
    def __init__(self, preco):
        self._preco = preco  # Atributo privado

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo")
        self._preco = novo_preco

    @preco.deleter
    def preco(self):
        del self._preco

# Usando a classe
produto = Produto(100)
print(produto.preco)  # Acessando como um atributo

produto.preco = 150  # Modificando o valor com o setter
print(produto.preco)

#------------------------------------------------------------------------------------------------------
self.nome = nome.title() # se colocarmos tible todas as palavras criadas na instanciação da classe vai começar com letra maiuscula

'''
O decorador @classmethod em Python é usado para definir um método de classe, que é um método 
que pertence à classe em vez de a uma instância específica da classe. Ele recebe a 
classe como seu primeiro argumento, comumente chamado de cls, em vez da instância (self).
'''

class Produto:
    taxa_desconto = 0.10  # Atributo de classe
    
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @classmethod
    def alterar_taxa_desconto(cls, nova_taxa):
        cls.taxa_desconto = nova_taxa
    
    def preco_com_desconto(self):
        return self.preco * (1 - self.__class__.taxa_desconto)

# Criando instâncias da classe Produto
produto1 = Produto('Notebook', 3000)
produto2 = Produto('Smartphone', 1500)

print(f"Taxa de desconto inicial: {Produto.taxa_desconto}")
print(f"Preço com desconto do produto1: {produto1.preco_com_desconto()}")
print(f"Preço com desconto do produto2: {produto2.preco_com_desconto()}")

# Alterando a taxa de desconto usando o método de classe
Produto.alterar_taxa_desconto(0.20)

print(f"Nova taxa de desconto: {Produto.taxa_desconto}")
print(f"Novo preço com desconto do produto1: {produto1.preco_com_desconto()}")
print(f"Novo preço com desconto do produto2: {produto2.preco_com_desconto()}")

#---------------------------------------------------------------------------------------------
