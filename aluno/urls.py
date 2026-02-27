from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_aluno'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('update/<int:id>', views.atualizar, name='atualizar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
]
