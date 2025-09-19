from django.contrib import admin
from django.urls import path, include
from appteste import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),       # página inicial
    path('produtos/', include('appteste.urls'))  # tudo que for de produtos começa com /produtos/
]
