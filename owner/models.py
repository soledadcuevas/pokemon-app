from django.db import models

class Owner(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    pais = models.CharField(max_length=27, default='')
    dni = models.CharField(max_length=8, default='00000000')
    vigente = models.BooleanField(default=True)



# Create your models here.
