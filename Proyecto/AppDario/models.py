from django.db import models

# Create your models here.
class Cursos(models.Model):

    nombre = models.CharField(max_length=40)
    duracion = models.CharField(max_length=30)

class Newsletters(models.Model):

    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

class Tarifario(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

