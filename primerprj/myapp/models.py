from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    inscriptos = models.IntegerField()
    solo_empresas = models.BooleanField(default=False)
    TURNOS = (
        ("M", "Mañana"),
        ("T", "Tarde"),
        ("N", "Noche")
    )
    turno = models.CharField(choices=TURNOS, null=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField(null=True)
    profesion = models.CharField(max_length=40)    
    edad = models.IntegerField(default=0)  