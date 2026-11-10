from django.shortcuts import render
from .models import Produto

def inicio(request):
    contexto={
        'nome_projeto': 'Loverary & Brew',
        'descricao': 'Um espaço híbrido aconchegante que combina livraria, cafeteria e floricultura.',
    }
    return render(request, 'principal/inicio.html', contexto)

def lista_produtos(request):
    produtos=Produto.objects.filter(disponivel=True)
    contexto={
        'produtos': produtos
    }
    return render(request, 'principal/produtos.html', contexto)