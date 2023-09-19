As técnicas de machine learning podem ser divididas em duas categorias principais: 
aprendizado supervisionado (acompanhado) e 
aprendizado não supervisionado (não acompanhado). 

Aqui estão algumas técnicas comuns em ambas as categorias:

Aprendizado Supervisionado (Acompanhado):
Nesse tipo de aprendizado, o modelo é treinado em um conjunto de dados rotulado, onde os exemplos de entrada possuem rótulos conhecidos. O objetivo é aprender uma relação entre as entradas e os rótulos para fazer previsões em novos dados.

Regressão Linear: Prevê valores contínuos (por exemplo, prever o preço de uma casa com base em suas características).
Regressão Logística: Utilizada para problemas de classificação binária (prever uma entre duas classes possíveis).
Árvores de Decisão: Estruturas hierárquicas que tomam decisões dividindo as características em nós de decisão.
Random Forest: Conjunto de árvores de decisão, fornecendo maior precisão e robustez.
Support Vector Machines (SVM): Classificação de dados separando-os com hiperplanos otimizados.
Redes Neurais Artificiais: Modelos que simulam o funcionamento do cérebro humano, usados em problemas complexos.

Quantitativo: representam os dados numéricos.
Discretos: representam uma contagem na qual os valores possíveis formam um conjunto finito ou enumerável. Por exemplo: número de filhos, quantidade de cursos realizados, quantidade de lugares frequentados.
Contínuos: podem assumir qualquer valor em um intervalo de valores. Por exemplo: altura, tempo.

Qualitativo: representam dados que expressam qualidade, opinião ou ponto de vista.
Nominais: não existe uma ordenação entre as categorias. Por exemplo: sexo, doente/sadio, cor dos olhos.
Ordinais: existe uma ordenação entre as categorias. Por exemplo: escolaridade, classe social.

Aprendizado Não Supervisionado (Não Acompanhado):
Aqui, o modelo é treinado em um conjunto de dados não rotulado e busca identificar padrões intrínsecos nos dados, como agrupamentos ou redução de dimensionalidade.

Clustering (Clasterização): Agrupamento de dados em clusters, como K-Means, Hierarchical Clustering, DBSCAN.
Anomaly Detection (Detecção de Anomalias): Identificação de pontos de dados que são diferentes do padrão geral.
Dimensionality Reduction (Redução de Dimensionalidade): Técnicas como PCA e t-SNE para reduzir a quantidade de variáveis mantendo as informações mais importantes.
Autoencoders: Técnicas de redes neurais para aprender representações compactas de dados.
Topic Modeling: Identificação de tópicos em conjuntos de documentos não rotulados.
Generative Adversarial Networks (GANs): Usadas para gerar novos dados com base em padrões aprendidos do conjunto de treinamento.
Association Rule Learning: Descoberta de padrões frequentes em conjuntos de dados transacionais.
Self-Organizing Maps (SOMs): Técnica de redução de dimensionalidade e visualização de dados.

Cada categoria tem seu próprio conjunto de técnicas que são adequadas para diferentes tipos de problemas. A escolha da técnica depende dos dados, dos objetivos do projeto e do tipo de insights que você deseja obter.

Classificação:

Regressão Logística
Árvores de Decisão
Random Forest
Support Vector Machines (SVM)
Naive Bayes
Redes Neurais

Regressão:
Regressão Linear
Regressão Polinomial
Ridge Regression
Lasso Regression
Elastic Net Regression
Support Vector Regression (SVR)

Técnicas de Séries Temporais:
ARIMA (Autoregressive Integrated Moving Average)
Modelos de Suavização Exponencial


Aprendizado Não Orientado (Não Supervisionado):
Nesse tipo de aprendizado, os algoritmos exploram padrões intrínsecos nos dados sem rótulos conhecidos.

Clustering (Clasterização):
K-Means
Hierarchical Clustering
DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
Mean Shift
Gaussian Mixture Models (GMM)

Redução de Dimensionalidade:
Principal Component Analysis (PCA)
t-Distributed Stochastic Neighbor Embedding (t-SNE)
Linear Discriminant Analysis (LDA)

Detecção de Anomalias:
Isolation Forest
One-Class SVM
Autoencoders

Mineração de Associação:
Apriori Algorithm
FP-Growth Algorithm

Tópicos em Modelos de Texto:
Latent Dirichlet Allocation (LDA)
Non-Negative Matrix Factorization (NMF)
Visualização de Dados:

Self-Organizing Maps (SOMs)
Hierarchical Embedding
Lembre-se de que essas são apenas algumas das técnicas disponíveis em cada categoria. 
A escolha da técnica depende dos objetivos do projeto, dos tipos de dados e do que você deseja extrair dos dados em questão.


_____________________________________________________________________________________________________________________________
uma organização util para os modelos de machine learn é dividi-los em aprendizado supervisionados e aprendizado não supervisionados
pode existir um mesmo modelo para ambos os tipos, porem com uma personalização em seu codigo que possibilite a utilização do modelo
tanto com uma classe ja determinada quanto sem a existencia dessa classe.

tambem é possivel ter uma certa distinção entre os modelos pelo problema que o modelo ajuda a resolver.
ai organizariamos os modelos por tipos preditivo, descritivo e prescritivo.

Problemas Preditivos (Predictive Problems):
Definição: Problemas preditivos são aqueles em que o objetivo é prever ou estimar um valor futuro ou desconhecido 
com base em dados históricos ou informações disponíveis. Isso envolve a construção de modelos que podem fazer previsões 
ou classificar novos dados com base em padrões e relacionamentos identificados nos dados de treinamento.
Exemplo: Prever o preço de uma casa com base em suas características, prever a probabilidade de um cliente comprar um produto,
 prever a demanda de produtos em um determinado período.

Regressão Linear: Usado para prever valores contínuos, como preços, temperaturas, etc.
Regressão Logística: Usado para classificação binária, como detecção de spam (sim/não).
Árvores de Decisão: Pode ser usado para classificação ou regressão.
Random Forest: Pode ser usado para classificação ou regressão, geralmente mais robusto que árvores de decisão individuais.
Gradient Boosting (por exemplo, XGBoost, LightGBM): Usado para melhorar o desempenho em problemas de classificação e regressão.
Redes Neurais Artificiais (Deep Learning): Usado em uma ampla variedade de problemas, incluindo visão computacional e processamento de linguagem natural.


Problemas Descritivos (Descriptive Problems):
Problemas descritivos envolvem a exploração e a análise de dados para obter insights, padrões ou estruturas subjacentes 
nos dados. O objetivo é compreender e descrever os dados de maneira significativa, muitas vezes por meio de técnicas de 
visualização ou redução de dimensionalidade.
Exemplo: Agrupar clientes com base em seu comportamento de compra, identificar os principais fatores que afetam o desempenho 
de vendas de uma empresa, resumir a estrutura subjacente dos dados de pesquisa de mercado
Análise de Componentes Principais (PCA): Usado para redução de dimensionalidade e análise exploratória.
Análise de Cluster (por exemplo, K-Means, DBSCAN): Usado para agrupar dados semelhantes.
Análise de Séries Temporais: Usado para modelar dados sequenciais, como previsão de vendas ao longo do tempo.
Análise de Texto: Usado para extrair informações de texto, como tópicos ou sentimentos.


Problemas Prescritivos (Prescriptive Problems):
Definição: Problemas prescritivos envolvem a determinação da melhor ação ou decisão a ser tomada com base em dados e modelos. 
Isso inclui a otimização de processos, a recomendação de ações ou a escolha da melhor solução para um determinado problema 
com o objetivo de alcançar um resultado desejado.
Exemplo: Recomendar produtos aos clientes com base em seu histórico de compras, otimizar a rota de entrega de veículos 
de transporte, determinar a alocação ideal de recursos em uma empresa.

Algoritmos de Recomendação: Usado para recomendar produtos, conteúdo ou itens com base no histórico do usuário.
Otimização: Usado para encontrar a melhor solução em cenários complexos, como programação linear ou otimização de rota.
Aprendizado por Reforço: Usado em ambientes de tomada de decisão sequencial, como jogos ou controle de robôs

