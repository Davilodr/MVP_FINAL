
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required

from Users.models import Perfil

from .form import AvatarForm, PerfilUserCreationForm, UserEditForm


def Index(request):
    
        return render(request, "index.html")


def loginview(request):
    
    if request.method == 'POST':

        Formulariologin = AuthenticationForm(request, data=request.POST)

        if Formulariologin.is_valid():
            
            data = Formulariologin.cleaned_data
            
            usuario = data["username"]
            psw = data["password"]
            
            user = authenticate(username = usuario, password = psw)
            
            if user:
                
                login(request, user)
                
                return render(request, "index.html",{"url": user.Avatar.url})
            else:
                return render(request, "index.html", {"mensaje": f'Error, los datos ingresados son incorrectos'})
        
        return render(request, "index.html",{"mensaje": f'Error, formulario invalido'}) 
    else:

        Formulariologin = AuthenticationForm()

        return render(request, "login.html", {"FormularioLogin": Formulariologin})

def rigistrarse(request):
    
    if request.method == 'POST':

        Formularioregistro = PerfilUserCreationForm(request.POST)

        if Formularioregistro.is_valid():

            username = Formularioregistro.cleaned_data["username"]
            
            Formularioregistro.save()
                        
            return render(request, "index.html", {"mensaje": f'Usuario {username} creado con exito'})     
        else:
            return render(request, "index.html",{"mensaje": f'Error, al crear el usuario'})
    else:
        

        Formularioregistro = PerfilUserCreationForm()

        return render(request, "registrarse.html", {"FormularioRegistro": Formularioregistro})

def editar_perfil(request):
    
    usuario = request.user

    if request.method == 'POST':
            
        editform = UserEditForm(request.POST)

        if editform.is_valid():
           
            data = editform.cleaned_data
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
        
            usuario.save()
            
            return render(request, "index.html", {"mensaje": f'Datos actualizados!'})
        
        return render(request, "index.html", {"mensaje": 'Contraseñas no coinciden'} )
    
    else:

        editform = UserEditForm(instance=request.user)
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "editarPerfil.html", {"editform": editform, "url": avatar.Avatar.url})

@login_required
def edit_avatar(request):
    profile = Perfil.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        avatar = AvatarForm(request.POST, request.FILES, instance=profile)
        if avatar.is_valid():
            avatar.save(commit = False)
            avatar.save()
            
        return render(request, "index.html",{"mensaje": f'Avatar actualizado!',})
    else:
        avatar=AvatarForm()   
        
        return render(request, "editar_avatar.html", {"avatar":avatar})