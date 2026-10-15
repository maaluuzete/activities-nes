from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome=models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    data_publicacao = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao_prevista = models.DateField()
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        status="Devolvido" if self.devolvido else "Ativo/Atrasado"
        return f"Empréstimo de {self.livro.titulo} para {self.usuario.username} ({status})"