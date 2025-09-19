from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
        ("Eletronicos", "Eletrônicos"),
        ("Roupas", "Roupas"),
        ("Alimentos", "Alimentos"),
        ("Outros", "Outros"),
    ]
    
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField()
    quantidade_estoque = models.IntegerField()
    url = models.URLField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    
    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()


