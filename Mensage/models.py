from django.conf import settings
from django.db import models

# Create your models here.

class Sugerencia(models.Model):
    
    nombre = models.CharField(max_length=50)
    mensaje_id =models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Id_mensaje_personal"), on_delete=models.CASCADE)
    mensaje = models.TextField()
    dia_actual = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.dia_actual} - Nombre:{self.nombre}'