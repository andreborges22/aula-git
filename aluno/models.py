from django.db import models
from curso.models import Curso

# Create your models here.


class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=100, default="sem@email.com")
    nascimento = models.DateField(null=True)    

    def __str__(self):
        return self.nome
