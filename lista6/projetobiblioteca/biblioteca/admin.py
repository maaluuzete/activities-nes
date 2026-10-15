from django.contrib import admin
from .models import Categoria, Autor, Livro, Emprestimo

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display=('nome', 'descricao')
    search_fields=('nome',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display=('nome', 'email')
    search_fields=('nome', 'email')

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display=('titulo', 'isbn', 'data_publicacao', 'categoria')
    list_filter=('categoria', 'data_publicacao')
    search_fields=('titulo', 'isbn')

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display=('usuario', 'livro', 'data_emprestimo', 'data_devolucao_prevista', 'devolvido')
    list_filter=('devolvido', 'data_emprestimo')
    search_fields=('usuario__username', 'livro__titulo')