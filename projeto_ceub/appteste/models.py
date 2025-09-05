from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return f'Produto: {self.nome}-{self.preco}'

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()


