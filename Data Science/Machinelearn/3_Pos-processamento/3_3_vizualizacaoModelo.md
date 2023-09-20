quando criamos um modelo e matematicamente esse modelo esta bem validado temos que entender quais variaveis 
são importante para o modelo ate mesmo para desenvolver solução no BI. tipo é importante saber quais features 
geram mais impacto no modelo.

é preciso ter esse entendimento de forma visual.

no primeiro exemplo estou utilizando o scatter do matplotlib:
'''py'''
import matplotlib.pyplot as plt

plt.scatter(dados["PURCHASES"], dados["PAYMENTS"],c=modelo, s=5, cmap='rainbow')
'''py'''
scatter = grafico de pontos
primeiro é escolhido 2 features
c = deve ser colocado o clusters separado ou uma classificação.
s = o tamanho dos pontos
cmap = a paleta de cores.

no segundo exemplo foi utilizado o seaborn que mostra varios grafico de uma vez so.
import seaborn as sns
dados["cluster"] = modelo
sns.pairplot(dados[0:],hue="cluster")

no primeiro passo criamos uma nova coluna no dataframe destinada para o cluster
depois chamados o pairplot 
dados[0:] = detemina que queremos ver todas as features
hue = escolhe qual coluna vai determinar as cores do grafico