from django.shortcuts import render
from .models import Produto

def index(request):
    return render(request, 'meu_app/index.html', {})

def sobre(request):
    return render(request, 'meu_app/sobre.html', {})

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'meu_app/lista.html', {'produtos': produtos})
    
def detail_product(request, id):
    produto = None
    msg = ''
    try:    
        produtos = Produto.objects.get(pk=id)
    except:
        msg = 'Produto inexistente na Base de Dados.'
    return render(request, 'meu_app/detail_product.html', {'produtos': produtos, 'msg': msg})

def contatos(request):
    return render(request, 'meu_app/contato.html', {})
