from django.db import models

from appMedi.models.familiar import Familiar
from appMedi.models.persona import Persona
from appMedi.models.personalMedico import Personalmedico
class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=256)
    ciudad = models.CharField(max_length=256)
    fecha_de_nacimiento = models.DateField()
    estatura = models.CharField(max_length=20)
    peso = models.CharField(max_length=20)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    familiar =  models.ForeignKey(Familiar, on_delete=models.CASCADE, null=True, blank=True)
    personalMedico= models.ForeignKey(Personalmedico, on_delete=models.CASCADE, null=True, blank=True)
    
    