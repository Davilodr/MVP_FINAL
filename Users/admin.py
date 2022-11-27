from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 

from .form import PerfilUserCreationForm, UserEditForm

from .models import  Administrador, Perfil


# Register your models here.

admin.site.register(Perfil)
admin.site.register(Administrador)


