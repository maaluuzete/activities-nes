from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro
from django.contrib.auth.decorators import login_required
from .models import Emprestimo

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/lista.html', {'livros': livros})

def detalhe_livro(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    return render(request, 'biblioteca/detalhe.html', {'livro': livro})

@login_required
def registrar_emprestimo(request, livro_id):
    livro = get_object_or_404(Livro, pk=livro_id)
    
    emprestimo_ativo = Emprestimo.objects.filter(livro=livro, devolvido=False).exists()
    
    if emprestimo_ativo:
        return render(request, 'biblioteca/detalhe.html', {
            'livro': livro,
            'erro': 'Este livro já se encontra emprestado no momento.'
        })
    
    if request.method == 'POST':
        data_devolucao = request.POST.get('data_devolucao_prevista')
        Emprestimo.objects.create(
            usuario=request.user,
            livro=livro,
            data_devolucao_prevista=data_devolucao,
            devolvido=False
        )
        return redirect('biblioteca:listar_livros')
        
    return render(request, 'biblioteca/emprestar.html', {'livro': livro})