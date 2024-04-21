antes de tudo vamos atualizar todas as bibliotecas dentro do ambiente virtual e do linux:

python -m pip install --upgrade pip
sudo apt update
sudo apt upgrade
sudo apt dist-upgrade
sudo apt autoremove
--------------------------------------------------------------
dentro do ambiente virtual vamos instalar o django
pip install django
python -m django --version ou pip list
-----------------------------------------------------------------
com o comando:
django-admin help // podemos ver todos os comando que podemos dar na ferramenta.
django-admin startproject setup . // setup é o nome da pasta. se nao colocar o ponto no final vai criar duas pasta setup #startproject // vai criar uma pasta setup com todos os arquivos de novo projeto.

criando um aplicativo
python manage.py startapp meu_aplicativo SETUP/meu_aplicativo
python manage.py startapp login SETUP/login
---- caso o comando acima nao der certo export PYTHONPATH=$PYTHONPATH:~/Python/Django/Projeto02/EFMOPSEG$ # use esse para colocar a pasta no PYTHONPATH
echo $PYTHONPATH # para ver se o caminho esta no pythonpath
~/.bashrc # esse comando reinicia o terminal ?
pip install freeze
pip freeze > requirements.txt # esse comando salva as bibliotecas utilizadas.
pip install -r requirements.txt -- para instalar as bibliotecas
python manage.py runserver
apos mudar o arquivo venv de diretorio tive alguns problemas para instalar bibliotecas:
nano caminho_para_venv/bin/activate # usei esse comando para mudar o diretorio do venv
e tive que alterar a primeira linha de todos os arquivos dentro de venv, pois estava pegando o diretorio antigo
which python # para saber em qual virtualização vc esta.
--------------------------------------------------------------------------
para fazermos o versonamento precisamos tirar a chave secreta que existe dentro do arquivo settings.py

para isso vamos criar uma função dentro do script settings.py e para essa função temos que baixar a biblioteca:
pip install python-dotenv.

colocaremos a seguinte função no settings:
from pathlib import Path, os
from dotenv import load_dotenv

load_dotenv()
e no lugar onde estava a nossa secret key vamos chamar essa função
str(os.getenv('SECRET_KEY'))

essa função ira acessar uma pasta que nao vai pro github, essa pasta é chamada de .env e ela sim tem a chave secreta.

vamos criar um arquivo chamado .gitignore e dentro dele colocaremos o arquivo .env
--------------------------------------------------------------------------------------------------
paara rodar a pagina usamos o seguinte comando 
python manage.py runserver
python manage.py makemigrations
python manage.py migrate # atualiza a conexao do banco
netstat -ano | findstr :8080 # identifica o processo que esta usando a porta 8080
taskkill /F /PID 1234 # finaliza o processo
------------------------------------------------------------------------------------------------


manage.py:
O manage.py é um utilitário de linha de comando que permite interagir com seu projeto Django.
Ele é usado para realizar várias tarefas, como iniciar um servidor de desenvolvimento, criar migrações de banco de dados, criar superusuários, entre outras.
É usado principalmente durante o desenvolvimento do projeto e não é implantado em um ambiente de produção.
-------minha visão-------
vejo que o manage.py é um arquivo nescessario para a estrutura na biblioteca Django é usada pra rodar o metodo main que determina o settings.py como arquivos dentantor
das configurações do projeto

settings.py:
O settings.py contém as configurações do seu projeto Django.
Nele, você define coisas como a configuração do banco de dados, as chaves secretas, os aplicativos instalados, as configurações de internacionalização, entre outras.
É um arquivo fundamental para configurar e personalizar o comportamento do seu projeto Django.

views.py:
O views.py contém as funções de visualização (views) que processam as solicitações HTTP dos clientes e retornam respostas.
Cada função de visualização geralmente corresponde a uma URL específica do seu site e é responsável por retornar o conteúdo correto para essa URL.
As visualizações interagem com modelos para recuperar dados do banco de dados e com os templates para renderizar o conteúdo HTML a ser retornado ao cliente.

Arquivo urls.py:
Configure as rotas para essas views em seu arquivo urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicial/', views.inicial, name='inicial'),

----minha visao-----
dentro de url.py vamos acessar os metodos criados dentro do arquivo views.py
a sintax do codigo:
path('inicial'...) = é o nome do diretorio pagina aquele que fica na url(http://seusite.com/inicial/), quando vazio é a pagina raiz.
path(...'views.inicial'...) = esse é o metodos dentro de views.py que renderiza a pagina inicial.html 
path(...'name='inicial') = aqui ja é uma variavel para usarmos de link no codigo html/Django. para usar o link: {% url 'inicial' %}
--------------------------------------------------------------------------------------
