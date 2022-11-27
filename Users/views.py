
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
from Users.models import Administrador
from PControl.form import PersonalFormulario
from django.contrib.auth.models import Group


from Users.models import Perfil

from .form import Imageneditform, PerfilUserCreationForm, UserEditForm

def Home(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        
        return render(request, "Home.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Home.html")
        
def Sobre_Mi(request):
    
    return render(request, "Sobre_Mi.html")  

def Cargar_personal_logout(request):
    return render(request, "Registrar_logout.html")

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
                
                return render(request, "index.html",{"url": user.Avatar.url, "banner":user.banner.url})
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
@login_required
def editar_perfil(request):
    
    usuario = request.user

    if request.method == 'POST':
            
        editform = UserEditForm(request.POST, request.FILES)
    
        if editform.is_valid():
            
            data = editform.cleaned_data
            
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.banner = data ["banner"]
            usuario.save()
        
           
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html", {"mensaje": f'Datos actualizados!',"url":avatar.Avatar.url, "banner":avatar.banner.url})
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "index.html", {"mensaje": 'Contraseñas no coinciden'} )
    
    else:
        editform = UserEditForm(instance=request.user)
        
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "editarPerfil.html", {"editform": editform, "url": avatar.Avatar.url, "banner":avatar.banner.url})

def edit_avatar(request):
    profile = Perfil.objects.get(pk=request.user.pk)
    if request.method == 'POST':
        avatar = Imageneditform(request.POST, request.FILES, instance=profile)
        if avatar.is_valid():
            avatar.save(commit = False)
            avatar.save()
        ava = Perfil.objects.get(pk=request.user.pk)
        return render(request, "index.html",{"mensaje": f'Avatar actualizado!',"url": ava.Avatar.url, "banner":ava.banner.url})
    else:
        avatar=Imageneditform()   
        ava = Perfil.objects.get(pk=request.user.pk)
        return render(request, "editar_avatar.html", {"avatar":avatar,"url": ava.Avatar.url, "banner":ava.banner.url})

def Crear_User_Admin(request):
    
    if request.method == 'POST':

        info = (request.POST)
        
        PersonalForm = PersonalFormulario(
            {"nombre":info["nombre"],
             "apellido":info["apellido"],
             "dni":info["dni"],
             "email":info["email"],
             "telefono":info["telefono"],
             "direccion":info["direccion"]}  
        )
        
        userform = PerfilUserCreationForm(
            {"username":info["username"],
             "password1":info["password1"],
             "password2":info["password2"]}
        )
        
        if PersonalForm.is_valid() and userform.is_valid():

            data = PersonalForm.cleaned_data
            
            data.update(userform.cleaned_data)
                  
            user = Perfil(username = data["username"])
            user.set_password(data["password1"])

            Personal = Administrador(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], dni=data['dni'], telefono=data['telefono'], direccion=data['direccion'], 
            user_id=user)
            
            Super = Group.objects.get(name='admin')
            
            user.save()
            Personal.save()
            user.groups.add(Super)
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html", {"mensaje": f'Perfil creado con exito',"url": avatar.Avatar.url, "banner":avatar.banner.url})
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html",{"mensaje": f'Error, formulario invalido',"url": avatar.Avatar.url, "banner":avatar.banner.url})
    else:

        PersonalForm = PersonalFormulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        userform = PerfilUserCreationForm()

        return render(request, "FormularioAdministrador.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url, "banner":avatar.banner.url})