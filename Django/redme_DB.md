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

com o Django devemos obedecer a estrutura de ORM sempre, ou seja temos que ter nosso aplicativo dentro de INSTALLED_APPS = ['meu_app'], temos que criar uma class dentro de models, referenciando o banco essa classe é a orientação a objeto que faz o intermedio entre o banco e o codigo Django. com isso referenciamos um template para esse model.

a ideia nao é usar o ORM do Django, vamos manipular muito o banco de dados para depois exibi-lo eu ainda nao sei se pego o banco externo e coloco no banco interno, ou se trato todo os dados de tempos em tempos e crio tabelas internas para analises pontuais.

mas basicamente é possivel acessar o banco de dados com uma conexao normal usando o pyodbc vou usar essa conexao por hora como um metodo dentro de models.py que vai ser chamado pelo javascript em uma ação na pagina html.

-----------------------------------------------------------------------------------------------
aqui sera utilizado o banco de dados nativo do Django o SQLlite3. 
temos que garantir que o nome do aplicativo seja o mesmo em todas as camadas, principalmente em settings.py  onde em :
```Python
INSTALLED_APPS = [
    ...
    'Galeria',
    ...
]
```
isso ira criar uma pasta migrations e um arquivo 0001_initial.py que é um codigo python criando uma tabela no banco de dados. lembrando que usamos ORM em models para criar uma classe que referencia os atributos da classe com as colunas do banco de dados.
```Python
python manage.py migrate #por fim para realmente criar o banco de dados
```
vamos em views pegar a classe de models que corresponde ao banco de dados criado.
feito isso tambem vamos fazer com que o index.html possa varrer os dados atraveis da views.

logo a view é respondavel por acessar models que usa o ORM com o DB e renderiza a pagina index com os dados desse DB.

ja no index é colocado como vai ser feito a varredura desses dados. atraves de laços pelo proprio Django, 

uma outra integração que ocorre é que no arquivo index, podemos deixar uma referencia dinamica para cada click em uma imagem que ate entao abria uma unica pagina, e agora ela vai abrir paginas respectiva a foto clicada.
para isso em views na parte onde falamos que ao clicar na imagem vamos visitar uma outra pagina. ai temos uma referencia para o arquivo url.py, onde foi criado o path de acesso para a pagina imagem.

temos entao o arquivo imagem.html e dentro de url.py um path referenciando essa pagina, em index informamos o id da imagem que deve ser acessado casso clicado.

tipo teremos esse id pq essa informaçao esta no db puxamos essa informação ja renderizada na view, e dentro de index temos sim acesso ao id dessa linha do banco, percebe um ciclo ? onde a informação vem pra index e quando vamos sair de index precisamos passar por url.py para chegar em imagem.html usando as informações do banco.

 entao é acessado em views.py no medoto responsavel por renderizar a pagina imagem colocamos um atributo a mais no metodo que é o id

 ```python
 def imagem(request, foto_id):
    return render(request, 'galeria/imagem.html')
 ```

-------------------------------------------------------------------------------------------------
 
toda vez que criamos uma nova coluna na tabela temos que colocar os parametros dessa coluna em models ai vai ser criado um novo arquivo na pasta migrate e apos isso damos migrate no terminal, para que a nova coluna suba no banco.








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