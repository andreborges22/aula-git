from django.shortcuts import render, redirect
from .models import Aluno,Curso
# Create your views here.


def home(request):
    alunos = Aluno.objects.all()
    cursos = Curso.objects.all()
    return render(request, "aluno/home.html", {"alunos": alunos,"cursos": cursos})


def cadastrar(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    curso_id = request.POST.get("curso")
    Aluno.objects.create(nome=nome, email=email,curso_id = curso_id)
    return redirect(home)


def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    cursos = Curso.objects.all()
    return render(request, "aluno/update.html", {"aluno": aluno,"cursos":cursos})


def atualizar(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    curso_id = request.POST.get("curso")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.email = email
    aluno.curso_id = curso_id
    aluno.save()
    return redirect(home)

def deletar(request,id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect(home)