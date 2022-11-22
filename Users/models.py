from django.conf import settings
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, AbstractUser, User

class Perfil(AbstractUser):
    
    user_id = models.AutoField(db_column='user_id', primary_key=True)
    banner = models.ImageField(upload_to='banners', default='banners/banner.png', blank=True)
    Avatar = models.ImageField(upload_to='Avatares', default='Avatares/default.png', blank=True)
    
class Administrador(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'
