from django.shortcuts import render, redirect
from usuario.forms  import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    forms = LoginForms()

    if request.method == 'POST':
        forms = LoginForms(request.POST)

        if forms.is_valid():
            nome=forms['nome_login'].value()
            senha=forms['senha'].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.error(request, f'{nome} logado com sucesso!')   
            return redirect('index')
        else:
            return redirect('login') 
    return render(request, 'usuario/login.html',{"form":forms})

def cadastro(request):
    forms = CadastroForms()
    if request.method == 'POST':
        forms = CadastroForms(request.POST)

        if forms.is_valid():
            if forms['senha_1'].value() != forms['senha_2'].value():
                messages.error(request, 'senhas não são iguais')
                return redirect('cadastro')
            nome=forms['nome_cadastro'].value()
            email=forms['email'].value()
            senha=forms['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente')
                return redirect('cadastro')
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.error(request, 'Cadastro efetuado com sucesso')
            return redirect('login')
    return render(request, 'usuario/cadastro.html',{"form":forms})


def logout(request):
    auth.logout(request)
    messages.error(request, 'Logout efetuado com sucesso!')
    return redirect('login')