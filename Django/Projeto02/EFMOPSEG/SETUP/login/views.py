from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def inicial(request):
    return render(request, 'inicial.html')

def CadastroLocal(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)   
        return HttpResponse('Usuário criado com sucesso!')   

    return render(request, 'CadastroLocal.html')

def index_view(request):
        # Verificar qual botão foi clicado
        if request.POST.get('submit_type') == 'AD':
            # Autenticação AD
            pass
        elif request.POST.get('submit_type') == 'Local':
            # Redirecionar para a página de cadastro local
            return redirect('cadastro_local')
        return render(request, 'index.html')

     