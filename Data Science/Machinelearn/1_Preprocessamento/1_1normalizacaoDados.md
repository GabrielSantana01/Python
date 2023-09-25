na normalização do modelo foi usado o StandardScaler quanto que serve para deixar os valores das colunas com a mesma escala.

Normalizer (Normalização L2):

Use o Normalizer quando você deseja que todas as linhas dos seus dados tenham a mesma escala e sejam transformadas em vetores
 unitários (norma igual a 1).
É útil quando você está trabalhando com algoritmos que dependem de medidas de similaridade ou distância, como o K-Means, 
onde a magnitude das características pode afetar significativamente o resultado.
É apropriado quando você está interessado na direção dos vetores, mas não na magnitude das características.
Exemplo de uso: Normalização de dados de texto, análise de sentimentos, ou sempre que você quiser comparar a 
direção dos vetores, independentemente da magnitude.

StandardScaler (Padronização):

Use o StandardScaler quando você deseja que suas características tenham média zero e desvio padrão igual a 1.
É útil quando você está trabalhando com algoritmos que assumem que seus dados estão próximos de uma distribuição normal, 
como regressão linear, regressão logística, SVMs, etc.
Ajuda a lidar com outliers, porque leva em consideração a média e o desvio padrão, o que torna menos sensível a valores 
extremos.
no geral usa-se os 2 modelos e ver como reagi os modelos de ML.