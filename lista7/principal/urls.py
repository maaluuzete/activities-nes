from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
]