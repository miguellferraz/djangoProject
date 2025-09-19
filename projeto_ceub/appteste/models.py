from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    quantidade_estoque = models.IntegerField(default=0)
    url = models.URLField(blank=True, null=True)
    categoria = models.CharField(max_length=50)    
    
    def __str__(self):
        return f'Produto: {self.nome}-{self.preco}'

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()


