from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_aluno'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar'),
]
