from django.shortcuts import render

def index(request):
    return render(request, 'meu_app/index.html', {})

def sobre(request):
    return render(request, 'meu_app/sobre.html', {})
