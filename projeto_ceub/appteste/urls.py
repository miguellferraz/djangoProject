from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de view
    path('sobre', views.sobre, name='sobre'),
    path('produtos/', views.lista_produtos, name='listar_produtos'),
    path('contatos/', views.contatos, name='contatos'),
    path('detail_product/<int:id>', views.detail_product, name='detail_product'),
    path("cadastrar/", views.cadastrar_produto, name="cadastrar_produto"),
]

