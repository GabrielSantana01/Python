from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def inicial(request):
    return render(request, 'inicial.html')

def index_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('inicial')  # Redirecionar para a página inicial após o login
        else:
            # Autenticação falhou
            return render(request, 'index.html', {'error': 'Usuário ou senha inválidos'})
    else:
        return render(request, 'index.html')