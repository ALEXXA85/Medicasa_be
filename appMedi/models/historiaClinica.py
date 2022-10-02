from django.db import models

from appMedi.models.diagnostico import Diagnostico
from appMedi.models.paciente import Paciente
from appMedi.models.personalMedico import Personalmedico
from appMedi.models.signosVitales import Signosvitales

class Historiaclinica(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.TextField()
    paciente= models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True, blank=True)
    personalMedico= models.ForeignKey(Personalmedico, on_delete=models.CASCADE, null=True, blank=True)
    diagnostico= models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True, blank=True)
    Signosvitales= models.ForeignKey(Signosvitales, on_delete=models.CASCADE, null=True, blank=True)
