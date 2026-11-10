from django.db import models

class Categoria(models.Model):
    nome=models.CharField(max_length=100)
    descricao=models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome=models.CharField(max_length=150)
    descricao=models.TextField()
    preco=models.DecimalField(max_digits=8, decimal_places=2)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='produtos')
    disponivel=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"