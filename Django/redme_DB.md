gerenciando o acesso ao DB SQLServer

pip install django-pyodbc-azure

depois colocar em setting as configurações do banco
   'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'seu_banco_de_dados',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'seu_servidor_sql_server',
        'PORT': 'porta_sql_server',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },

sudo apt-get install unixodbc-dev # tive que instalar essa biblioteca tambem.

com o Django devemos obedecer a estrutura de ORM sempre, ou seja temos que ter nosso aplicativo dentro de INSTALLED_APPS = ['meu_app'], temos que criar uma class dentro de views, referenciando o banco essa classe é a orientação a objeto que faz o intermedio entre o banco e o codigo Django. com isso referenciamos um template para essa view.

a ideia nao é usar o ORM do Django, vamos manipular muito o banco de dados para depois exibi-lo eu ainda nao sei se pego o banco externo e coloco no banco interno, ou se trato todo os dados de tempos em tempos e crio tabelas internas para analises pontuais.

mas basicamente é possivel acessar o banco de dados com uma conexao normal usando o pyodbc vou usar essa conexao por hora como um metodo dentro de views.py que vai ser chamado pelo javascript em uma ação na pagina html.













------------------------------------------------------------------------------------------------
para instalar o driver ODBC Driver 17 for SQL Server precisei: 

sudo su
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
exit


sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17


sudo ACCEPT_EULA=Y apt-get install -y mssql-tools

echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc
source ~/.bashrc
-----------------------------------------------------------------------------------------------------
para instalar o driver SQL Server Native Client 11.0:

sudo apt-get update
sudo apt-get install -y unixodbc unixodbc-dev

baixei a versao correta no site da microsoft e extrair o arquivo tar.gz com o comando abaixo acessei a pasta extraida e tentei executar o arquivo install

tar -xzvf msodbcsql-11.0.2270.0.tar.gz
cd msodbcsql-11.0.2270.0

ainda faltava coisa:

sudo apt-get install -y libc6 libssl1.1 krb5-libs
sudo apt-get install -y unixodbc unixodbc-dev
sudo apt-get install -y libc6 libssl1.1
sudo apt-get install --reinstall unixodbc unixodbc-dev
sudo apt-get install unixodbc unixodbc-dev
sudo apt-get install libc6 libssl1.1
-----------------------------------------------------------------------------------------------