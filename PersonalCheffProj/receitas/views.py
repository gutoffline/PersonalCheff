from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receitas

def index(request):
    receitas = Receitas.objects.all()
    
    dados = {
        'lista_receitas' : receitas
    }
    
    return render(request,'index.html', dados)

def contato(request):
    return render(request,'contato.html')

def receita(request, receita_id):
    receita_bd = get_object_or_404(Receitas, pk=receita_id)
    receita_exibir={
        'uma_receita':receita_bd
    }
    return render(request,'receita.html', receita_exibir)
