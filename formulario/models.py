from django.db import models

# Create your models here.
from django.db import models
from cursos.models import Curso

class Inscripcion(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.curso.nombre}"
