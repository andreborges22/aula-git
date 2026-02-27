from django.shortcuts import render, redirect
from .models import Aluno
# Create your views here.


def home(request):
    alunos = Aluno.objects.all()
    return render(request, "aluno/home.html", {"alunos": alunos})


def cadastrar(request):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    Aluno.objects.create(nome=nome, email=email)
    return redirect(home)


def editar(request, id):
    aluno = Aluno.objects.get(id=id)
    return render(request, "aluno/update.html", {"aluno": aluno})


def atualizar(request, id):
    nome = request.POST.get("nome")
    email = request.POST.get("email")
    aluno = Aluno.objects.get(id=id)
    aluno.nome = nome
    aluno.email = email
    aluno.save()
    return redirect(home)

def deletar(request,id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect(home)