from email.policy import default
from random import choices
from django.db import models

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=256)
    apellidos = models.CharField(max_length=256)
    telefono = models.IntegerField()
    genero = models.CharField(max_length=15)