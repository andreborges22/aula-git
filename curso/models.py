from django.db import models
from professor.models import Professor

# Create your models here.


class Curso(models.Model):
    
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nome} ({self.carga_horaria} hora(s))"
