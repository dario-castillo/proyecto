from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    

class Pedido(models.Model):
    personaje = models.CharField(max_length=40)
    tecnica = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre    