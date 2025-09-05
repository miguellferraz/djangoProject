from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Exemplo de view
    path('sobre', views.sobre, name='sobre'),  # Exemplo de view
]
