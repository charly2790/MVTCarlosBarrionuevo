from django.db import models

# Create your models here.
class Familiares(models.Model):
    dni = models.IntegerField(unique=True)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    birthday = models.DateField(blank=True,null=True)

