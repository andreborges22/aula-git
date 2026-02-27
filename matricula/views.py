from django.shortcuts import render, redirect
from aluno.models import Aluno
from curso.models import Curso
from .models import Matricula
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.


def home(request):
    alunos = Aluno.objects.all()
    cursos = Curso.objects.all()
    return render(request, "matricula/home.html", {"alunos": alunos, "cursos": cursos})


def matricular(request):
    aluno_id = request.POST.get("aluno")
    curso_id = request.POST.get("curso")
    print("Aluno id", aluno_id)
    print("curso id", curso_id)
    aluno = Aluno.objects.get(id=aluno_id)
    try:
        Matricula.objects.create(aluno_id=aluno_id, curso_id=curso_id)
        messages.success(
            request, f"Estudante {aluno.nome} cadastrado(a) com sucesso!")
    except IntegrityError:
        messages.error(
            request, f"O Estudante {aluno.nome} já está matriculado nesse curso. Matrícula não efetuada!")

    return redirect(home)
