from django.shortcuts import render
from .models import teste01
def index(request):
    return render(request, 'index.html')

def imagem(request):
    return render(request, 'imagem.html')

def minha_view(request):
    registros = teste01.objects.using('default').all()
    return render(request, 'meu_template.html', {'registros': registros})
