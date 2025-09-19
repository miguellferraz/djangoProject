from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de view
    path('sobre', views.sobre, name='sobre'),
    path('produtos/', views.lista_produtos, name='listar_produtos'),
    path('contatos/', views.contatos, name='contatos'),
    path('detail_product/<int:id>', views.detail_product, name='detail_product'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    path('produtos/apagar/<int:id>/', views.apagar_produto, name='apagar_produto'),
]

