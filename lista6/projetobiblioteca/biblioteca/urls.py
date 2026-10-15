from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('livro/<int:livro_id>/', views.detalhe_livro, name='detalhe_livro'),
    path('livro/<int:livro_id>/emprestar/', views.registrar_emprestimo, name='registrar_emprestimo'),
]