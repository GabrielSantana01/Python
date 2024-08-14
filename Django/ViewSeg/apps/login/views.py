from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  logout
from apps.login.forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        nome = ''
        senha = ''
        if form.is_valid():
            nome = form['username'].value()
            senha = form['password'].value()

        usuario = authenticate(
            request,
            username=nome,
            password=senha
        )
        if not nome or not senha:
            messages.error(request, 'Por favor, preencha todos os campos.')
            return redirect('login')
        
        if usuario is not None:
            auth.login(request, usuario)
            return redirect('home')  # Redireciona após o login
        else:
            messages.error(request, 'usuário ou senha inválido')
            return redirect('login')

    return render(request, 'login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

def userlogout(request):
    logout(request)
    return redirect('login')