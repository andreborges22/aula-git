from django.db import models

# Create your models here.


class Curso(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.carga_horaria} hora(s))"
