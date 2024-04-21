from django.shortcuts import render
import pyodbc, os

# Create your views here.
def index(request):
    return render(request, 'index.html')



def consultar_banco_de_dados():
    # Configurações de conexão com o banco de dados
    server = str(os.getenv('server'))
    database = str(os.getenv('database'))
    username = str(os.getenv('username'))
    password = str(os.getenv('password'))
    
    # Conectando ao banco de dados
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

    # Criando um cursor
    cursor = conn.cursor()

    # Executando uma consulta SQL
    cursor.execute("SELECT TOP 1 * FROM [Runtime].[dbo].[AllTags_Live]")

    # Obtendo os resultados da consulta
    rows = cursor.fetchall()

    # Exibindo os resultados no terminal
    for row in rows:
        print(row)

    # Fechando o cursor e a conexão
    cursor.close()
    conn.close()

# Chamando a função para consultar o banco de dados
consultar_banco_de_dados()
