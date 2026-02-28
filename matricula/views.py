from django.shortcuts import render, redirect
from aluno.models import Aluno
from curso.models import Curso
from .models import Matricula
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.

#home principal
def home(request):
    #resgata todos os alunos do banco
    alunos = Aluno.objects.all()
    #resgata todos os cursos do banco
    cursos = Curso.objects.all()
    #renderiza a home enviando alunos e cursos
    return render(request, "matricula/home.html", {"alunos": alunos, "cursos": cursos})

#funcao para matricular
def matricular(request):
    #resgata o id do aluno
    aluno_id = request.POST.get("aluno")
    #resgata o id do curso
    curso_id = request.POST.get("curso")    
    #print("Aluno id", aluno_id)
    #print("curso id", curso_id)
    #resgata o aluno do banco
    aluno = Aluno.objects.get(id=aluno_id)
    try:
        #tenta realizar a insercao no banco
        Matricula.objects.create(aluno_id=aluno_id, curso_id=curso_id)
        #se deu certo, insere no objeto messages a mensagem de sucesso
        messages.success(
            request, f"Estudante {aluno.nome} cadastrado(a) com sucesso!")
    except IntegrityError:
        #se der errado, insere no objeto messages a mensagem de erro
        messages.error(
            request, f"O Estudante {aluno.nome} já está matriculado nesse curso. Matrícula não efetuada!")
    #redireciona para a home
    return redirect(home)
