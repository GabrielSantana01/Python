pode-se criar 3 tipos 

quando estiver trabalhando com a biblioteca atual o python:
usamos a biblioteca official para ambiente virtual o venv

para criar um ambienteVirtual usamos o seguinte comando:

py ou python -m venv nome 

--------------------------------------------------------------
caso esteja trabalhando com versões anteriores usamos outra biblioteca que
deve ser instalada no python.

install pyenv

python3.4 -m venv <nome>
-----------------------------------------------------------------------
para criar o ambiente virtual no vscode

primeiro tive que rodar:py -m venv venv

no diretorio atual:. venv/Scripts/activate
--------------------------------------------------------------------------
como estou usando o linux agora, pelo wsl consigo rodar o terminal linux pelo vscode instalado no windows.
e para abrir um ambiente virtual no terminal linux.

instalando ambiente virtual: pip3 install virtualenv
virtualenv --version
criar ambiente virtual: -m venv ambienteVirtual

ativando ambiente virtual: source ambienteVirtual/bin/activate

---------------------------------------------------------------------------------------
caso ultilize o powershell pode ocorrer um erro de permissoes. tem que digitar o seguinte comando:
Set-ExecutionPolicy RemoteSigned
Y ou A
-----------------------------------------------------------------------------------------
depois de muita briga e muito choro conseguir pensar em uma maneira de rodar o ambiente virtual sem o virtualenv. e sim com a biblioteca venv.
na linha de comando abaixo temos que acessar onde vai ficar o ambiente virtual e jogar o caminho da versao que queremos usar do python. apos isso usamos o -m e chamamos a biblioteca venv e damos um nome.
C:\caminho\para\python3.5.exe -m venv nome_do_ambiente_virtual

