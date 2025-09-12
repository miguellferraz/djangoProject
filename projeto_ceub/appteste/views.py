from django.shortcuts import render
from .models import Produto

def index(request):
    return render(request, 'meu_app/index.html', {})

def sobre(request):
    return render(request, 'meu_app/sobre.html', {})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'meu_app/lista.html', {'produtos': produtos})
    
def contatos(request):
    return render(request, 'meu_app/contato.html', {})

