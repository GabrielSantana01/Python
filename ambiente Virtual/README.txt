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


