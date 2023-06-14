from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

class Newsletters(models.Model):

    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)


