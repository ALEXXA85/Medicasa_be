from django.db import models

class Diagnostico(models.Model):
    id = models.AutoField(primary_key=True)
    fecha= models.DateField()
    recomendaciones= models.TextField()
    

