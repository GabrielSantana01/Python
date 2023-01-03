# Python
todos os estudos relacionados a python

para esse projeto vou trabalhar com git e github sincronizando tudo que for feito no jupyter notebook.
com isso foi criado uma organização de pastas em um repositorio no github, chamado python e foi criado uma pasta em documentos chamada python sincronizando todos os projetos dentro dessa pasta.

para usar o git é preciso acessar o diretorio de pasta no qual queremos trabalhar clicar com o direito do mouse e abrir o Git Bash Here
nesse promt iremos realizar os comandos para que e que os notebooks criado no jupyter seja enviado para o github e que os commits no git tb seja realizado

o primeiro comando é o git init para criar um repositorio local do git no diretorio que esta ocorrendo o trabalho. 
git init

o git add . adiciona seu projeto em um conteiner
git add .

o git status verifica o status desse conteiner " se algum arquivo foi alterado ou adicionado"
git status


o git commit pega o conteudo do conteiner e adiciona no repositorio local git criado no git init. o -m indica que o comando deve ter um comentario entre aspas.
git commit -m "first commit" 

o comando abaixo especifica as ramificações dos commits realizados, em qual ramo o comit estar, pois quando comitamos a podemos deixar uma versão como a original
-- e os demais commits ficam em ramos diferentes fazendo assim o versionamento. o HEAD é sempre o ultimo commit o master sempre o primeiro
git log --oneline --graph 


git branch -M main
git remote add origin url
git push -u origin main
git ls.files
