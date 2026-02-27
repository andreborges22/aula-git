from django.db import models
from aluno.models import Aluno
from curso.models import Curso

# Create your models here.
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    data_matricula = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.aluno} - {self.curso}"