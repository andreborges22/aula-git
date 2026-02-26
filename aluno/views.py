from django.shortcuts import render, redirect
from .models import Aluno
# Create your views here.


def home(request):
    alunos = Aluno.objects.all()
    return render(request, "aluno/home.html", {"alunos": alunos})

def cadastrar_aluno(request):
    nome = request.POST.get("nome")
    print(f"nome:{nome}")
    Aluno.objects.create(nome = nome)    
    return redirect(home)
