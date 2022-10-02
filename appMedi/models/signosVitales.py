from django.db import models
class Signosvitales(models.Model):
    id = models.AutoField(primary_key=True)
    oximetria = models.IntegerField()
    frec_respiratoria = models.IntegerField()
    frec_cardiaca = models.IntegerField()
    temperatura = models.IntegerField()
    presion_arterial = models.IntegerField()
    glucemias = models.IntegerField()
