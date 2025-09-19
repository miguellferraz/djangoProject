from django.shortcuts import get_object_or_404, redirect, render
from .models import Produto
from .forms import ProdutoForm

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

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'meu_app/lista_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'meu_app/adicionar_produto.html', {'form': form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'meu_app/form_produto.html', {'form': form})

def apagar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos')
