from django.shortcuts import render

def index(request):
    receitas = {
        1:'Suco de Melão',
        2:'Pizza',
        3:'Suco de Limão',
        4:'Suco de manga',
    }
    
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
