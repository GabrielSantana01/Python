from django.contrib.auth import authenticate

# Tente autenticar um usuário
user = authenticate(username='gabriel.santana', password='gsantana@evt')

if user is not None:
    # A autenticação foi bem-sucedida
    print('A autenticação foi bem-sucedida')
else:
    # A autenticação falhou
    print('A autenticação falhou')
