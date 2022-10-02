from django.db import models
from django.contrib.contenttypes.models import ContentType

from appMedi.models.persona import Persona
class Familiar(models.Model):
    id = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=256)
    correo = models.EmailField('Correo',max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)
    