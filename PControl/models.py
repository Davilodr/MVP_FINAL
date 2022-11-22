from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class PersonalCC(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    telefono= models.IntegerField()
    direccion=models.CharField(max_length=254)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'

class PersonalDXTV(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    telefono= models.IntegerField()
    direccion=models.CharField(max_length=254)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'
    
    

class Dias_trabajados(models.Model):
    
   
    dia_trabajado = models.DateField()
    personal = models.ForeignKey(PersonalCC,on_delete=models.CASCADE, related_name="Personal_PersonalCC")
    
    
    def __str__(self):
        return f'Dia Trabajado: {self.dia_trabajado} -- Personal: {self.personal.nombre}'
   

class Horas_trabajadas(models.Model):
    
    
    hora_trabajada = models.IntegerField()
    dia_actual = models.DateField(auto_now_add=True)
    personal1 = models.ForeignKey(PersonalDXTV, on_delete=models.CASCADE)
    
    
    
    def __str__(self):
        return f'{self.dia_actual} - {self.hora_trabajada} - {self.personal1.nombre}'
    
class Supervisor(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()
    email = models.EmailField(max_length=254)
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Dni:{self.dni} - Email: {self.email}'
