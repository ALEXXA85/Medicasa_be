from django.db import models

from appMedi.models.persona import Persona

class Personalmedico(models.Model):
    id = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=256)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
       