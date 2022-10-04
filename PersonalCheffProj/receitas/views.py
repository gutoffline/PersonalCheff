from django.shortcuts import render
from .models import Receitas

def index(request):
    receitas = Receitas.objects.all()
    
    dados = {
        'lista_receitas' : receitas
    }
    
    return render(request,'index.html', dados)

def contato(request):
    return render(request,'contato.html')

def sucodelaranja(request):
    return render(request,'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')
