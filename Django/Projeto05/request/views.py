from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def index(request):
    if request.method == "POST":
        data = json.loads(request.body)
        selecionado = data.get("selecionado", "")
        print('valor selecionado: '+ selecionado)
        return JsonResponse({"mensagem": "Seleção recebida com sucesso."})
    return JsonResponse({"erro": "Requisição inválida."}, status=400)