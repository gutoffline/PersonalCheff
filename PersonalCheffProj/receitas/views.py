from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def contato(request):
    return render(request,'contato.html')

def sucodelaranja(request):
    return render(request,'sucodelaranja.html')

def sucodelimao(request):
    return render(request, 'sucodelimao.html')
