from django.shortcuts import redirect, render
from django.contrib.auth.models import Group



from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from Users.models import Perfil

from Users.form import PerfilUserCreationForm

from .form import Dias_Formulario, Horas_Formulario, PersonalFormulario, UpdateDia_Form, Updatehoras_Form


from .models import Dias_trabajados, Horas_trabajadas, PersonalCC, PersonalDXTV, Supervisor
from django.views.generic import ListView

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator



def Index(request):
    
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        
        return render(request, "index.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "index.html")
        
def Cargar_Personal(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Cargar_Personal.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Cargar_Personal.html")
def About(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "About.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "About.html")
def Crear_Datos(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Crear_Datos.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
         return render(request, "Crear_Datos.html")
def Listar_Personal(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Lista_Personal.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Lista_Personal.html")
def Buscar_datos(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_datos.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Buscar_datos.html")
def Buscar_dias(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_dias.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Buscar_dias.html")

def Buscar_personalCC(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalCC.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Buscar_personalCC.html")
def Buscar_personalDXTV(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalDXTV.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    except:
        return render(request, "Buscar_personalDXTV.html")


def BuscarP(request):
    
    if request.GET["dni"]:

        try:
            dni_buscada = request.GET["dni"]
            personal = PersonalCC.objects.get(dni=dni_buscada)
            avatar = Perfil.objects.get(pk=request.user.pk)

            return render(request, "Resultado_BuscarPCC.html", {"Personal": personal, "Dni": dni_buscada, "url": avatar.Avatar.url, "banner":avatar.banner.url})
        except:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "Buscar_personalCC.html", {"mensaje": f'El dni ingresado no pertenece a Control Central', "url": avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalDXTV.html", {"mensaje": f'Los datos ingresados son incorrectos', "url": avatar.Avatar.url, "banner":avatar.banner.url})

def BuscarD(request):
   
    
    if request.GET["dni"]:
        try:
            dni_buscada = request.GET["dni"]
            personal = PersonalDXTV.objects.get(dni=dni_buscada)
            avatar = Perfil.objects.get(pk=request.user.pk)
                   
            return render(request, "Resultado_BuscarPDX.html", {"Personal": personal, "Dni": dni_buscada, "url": avatar.Avatar.url, "banner":avatar.banner.url})
        except:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "Buscar_personalDXTV.html", {"mensaje": f'El dni ingresado no pertenece a DXTV', "url": avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalDXTV.html", {"mensaje": f'Los datos ingresados son incorrectos', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        

def Crear_User_PersonalCC(request):
    
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

            Personal = PersonalCC(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], dni=data['dni'], telefono=data['telefono'], direccion=data['direccion'],  
            user_id=user)
            
            ControlCentral = Group.objects.get(name='ControlCentral')
            user.save()
            Personal.save()
            user.groups.add(ControlCentral)
            avatar = Perfil.objects.get(pk=request.user.pk)                       
            return render(request, "index.html", {"mensaje": f'Perfil creado con exito', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html",{"mensaje": f'Error, formulario invalido', "url": avatar.Avatar.url, "banner":avatar.banner.url})      
    else:

        PersonalForm = PersonalFormulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        userform = PerfilUserCreationForm()

        return render(request, "personal_formularioCC.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url, "banner":avatar.banner.url})

def Crear_User_PersonalDXTV(request):
    
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

            Personal = PersonalDXTV(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], dni=data['dni'], telefono=data['telefono'], direccion=data['direccion'], 
            user_id=user)
            
            DXtv = Group.objects.get(name='DXTV')
            
            user.save()
            Personal.save()
            user.groups.add(DXtv)
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html", {"mensaje": f'Perfil creado con exito', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html",{"mensaje": f'Error, formulario invalido', "url": avatar.Avatar.url, "banner":avatar.banner.url})
    else:

        PersonalForm = PersonalFormulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        userform = PerfilUserCreationForm()

        return render(request, "personal_formularioDXTV.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url, "banner":avatar.banner.url})

def Crear_User_Supervisor(request):
    
    if request.method == 'POST':

        info = (request.POST)
        
        PersonalForm = PersonalFormulario(
            {"nombre":info["nombre"],
             "apellido":info["apellido"],
             "dni":info["dni"],
             "email":info["email"]}  
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

            Personal = Supervisor(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], dni=data['dni'], 
            user_id=user)
            
            Super = Group.objects.get(name='Supervisor')
            
            user.save()
            Personal.save()
            user.groups.add(Super)
            
            return render(request, "index.html", {"mensaje": f'Perfil creado con exito'})
        else:
            return render(request, "index.html",{"mensaje": f'Error, formulario invalido'})
    else:

        PersonalForm = PersonalFormulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        userform = PerfilUserCreationForm()

        return render(request, "FormularioSupervisor.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url, "banner":avatar.banner.url})

def Listar_dias(request):
    
    diast = Dias_trabajados.objects.all()
    page = request.GET.get  ('page', 1)
   
    try:
        paginator=Paginator(diast, 5)
        diast =paginator.page(page)
        
    except:
        render(request, "Lista_dias.html")
    
    avatar = Perfil.objects.get(pk=request.user.pk)
    return render(request, "Lista_dias.html", {"diast":diast, "page_obj" :diast, "url":avatar.Avatar.url, "banner":avatar.banner.url})

def filtrarD(request, id):
        
        nombreDT = Dias_trabajados.objects.filter(personal = id)
        page = request.GET.get  ('page', 1)
        nombreDT = nombreDT.values("personal")
        nombreDT = nombreDT.values()
        try:
            paginator=Paginator(nombreDT, 5)
            nombreDT =paginator.page(page)
        
        except:
            render(request, "Lista_dias.html")
        avatar = Perfil.objects.get(pk=request.user.pk)             
        return render(request, "diascc.html",{"diast":nombreDT,"page_obj":nombreDT, "url":avatar.Avatar.url, "banner":avatar.banner.url})
    
def crear_dias(request):
    
    if request.method == 'POST':
        
        diasform= Dias_Formulario(request.POST)
        
        if diasform.is_valid():
            
            info = diasform.cleaned_data
            
            dia= Dias_trabajados(dia_trabajado=info['dia_trabajado'], personal=info['personal'])
            dia.save()
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render (request, "index.html", {"mensaje": f'Dia creado con exito',"url":avatar.Avatar.url, "banner":avatar.banner.url})  
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html", {"mensaje": f'Datos ingresados invalidos',"url":avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        
        dias_form = Dias_Formulario
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Crear_dias.html", {"forms": dias_form, "url":avatar.Avatar.url, "banner":avatar.banner.url})
     
def editar_dias(request, id):
    
    dia_trabajado = Dias_trabajados.objects.get(id=id)
    
    if request.method == 'POST':
            
        editform = UpdateDia_Form(request.POST)

        if editform.is_valid():
           
            data = editform.cleaned_data
            
            dia_trabajado.dia_trabajado = data["dia_trabajado"]
            dia_trabajado.personal = data["personal"]
            
            
        
            dia_trabajado.save()
            
            avatar = Perfil.objects.get(pk=request.user.pk) 
            return render(request, "index.html", {"mensaje": f'Datos actualizados!', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        
        avatar = Perfil.objects.get(pk=request.user.pk) 
        return render(request, "index.html", {"mensaje": 'Datos ingresados incorrectos', "url": avatar.Avatar.url, "banner":avatar.banner.url} )
    
    else:

        editform = UpdateDia_Form(initial={"dia_trabajado":dia_trabajado.dia_trabajado, "personal":dia_trabajado.personal})
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "Actualizar_dias.html", {"editform": editform, "url": avatar.Avatar.url, "banner":avatar.banner.url})     

def Borrar_dias(request, id):
    
    if request.method == 'POST':
        
        dia_trabajado = Dias_trabajados.objects.get(id=id)
        dia_trabajado.delete()
        
        dia_trabajado = Dias_trabajados.objects.all()
        page = request.GET.get  ('page', 1)
        try:
            paginator=Paginator(dia_trabajado, 5)
            dia_trabajado =paginator.page(page)
        
        except:
            render(request, "Lista_dias.html")
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "index.html",{"mensaje":f'Dia borrado con exito', "url": avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Borrar_dias.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
        
def Listar_horas(request):
    
    horast = Horas_trabajadas.objects.all()
    
    page = request.GET.get  ('page', 1)
    
    try:
        paginator=Paginator(horast, 8)
        horast =paginator.page(page)
        
    except:
       
        render(request, "Lista_Horas.html")
    
    avatar = Perfil.objects.get(pk=request.user.pk)
    return render(request, "Lista_Horas.html", {"horast":horast, "page_obj" :horast, "url":avatar.Avatar.url, "banner":avatar.banner.url})

def filtrarH(request, id):
        
        nombreHT = Horas_trabajadas.objects.filter(personal1 = id)
        page = request.GET.get  ('page', 1)
        nombreHT = nombreHT.values("personal1")
        nombreHT = nombreHT.values()
        try:
            paginator=Paginator(nombreHT,8)
            nombreHT =paginator.page(page)
        
        except:
            
            render(request, "Lista_Horas.html")
        
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "horasDXTV.html",{"horast":nombreHT, "page_obj" :nombreHT, "url":avatar.Avatar.url, "banner":avatar.banner.url})
    
def crear_horas(request):
    
    if request.method == 'POST':
        
        horas_form= Horas_Formulario(request.POST)
        
        if horas_form.is_valid():
            
            info = horas_form.cleaned_data
            
            hora= Horas_trabajadas(hora_trabajada=info['hora_trabajada'], personal1=info['personal1'])
            hora.save()
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render (request, "index.html", {"mensaje": f'Horas cargadas con exito',"url":avatar.Avatar.url, "banner":avatar.banner.url})  
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html", {"mensaje": f'Datos ingresados invalidos',"url":avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        
        horas_form = Horas_Formulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Crear_Hora.html", {"forms": horas_form, "url":avatar.Avatar.url, "banner":avatar.banner.url})
     
def editar_horas(request, id):
    
    horas_trabajadas = Horas_trabajadas.objects.get(id=id)
    
    if request.method == 'POST':
            
        editform = Updatehoras_Form(request.POST)

        if editform.is_valid():
           
            data = editform.cleaned_data
            
            horas_trabajadas.hora_trabajada = data["hora_trabajada"]
            
            horas_trabajadas.personal1 = data["personal1"]
            
            
        
            horas_trabajadas.save()
            
            avatar = Perfil.objects.get(pk=request.user.pk) 
            return render(request, "index.html", {"mensaje": f'Datos actualizados!', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        
        avatar = Perfil.objects.get(pk=request.user.pk) 
        return render(request, "index.html", {"mensaje": 'Datos ingresados incorrectos', "url": avatar.Avatar.url, "banner":avatar.banner.url} )
    
    else:

        editform = Updatehoras_Form(initial={"hora_trabajada":horas_trabajadas.hora_trabajada, "personal1":horas_trabajadas.personal1})
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "Actualizar_horas.html", {"editform": editform, "url": avatar.Avatar.url, "banner":avatar.banner.url})       

def Borrar_horas(request, id):
    
    if request.method == 'POST':
    
        horas_trabajadas = Horas_trabajadas.objects.get(id=id)
        horas_trabajadas.delete()
    
        horas = Horas_trabajadas.objects.all()
        page = request.GET.get('page', 1)
    
        try:
            paginator=Paginator(horas, 8)
            horas=paginator.page(page)
        
        except:
       
            render(request, "Lista_Horas.html")
        avatar = Perfil.objects.get(pk=request.user.pk)
        
        return render(request, "index.html",{"mensaje":f'Horas borradas con exito',"url": avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Borrar_horas.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})
    
def Listar_PersonalCC(request):
    
    personalCC = PersonalCC.objects.all()
    
    page = request.GET.get  ('page', 1)
    
    try:
        paginator=Paginator(personalCC, 8)
        personalCC =paginator.page(page)
        
    except:
       
        render(request, "Lista_Horas.html")
    
    avatar = Perfil.objects.get(pk=request.user.pk)
    return render(request, "Lista_PersonalCC.html", {"perCC":personalCC, "page_obj" :personalCC, "url":avatar.Avatar.url, "banner":avatar.banner.url})
  
def editar_PersonalCC(request, id):
    
    personal = PersonalCC.objects.get(id=id)
    
    if request.method == 'POST':
            
        editform = PersonalFormulario(request.POST)

        if editform.is_valid():
           
            data = editform.cleaned_data
            
            personal.nombre=data["nombre"]
            personal.apellido=data["apellido"]
            personal.dni=data["dni"]
            personal.email=data["email"]
            personal.telefono=data["telefono"]
            personal.direccion=data["direccion"]         
            
            personal.save()
            
            avatar = Perfil.objects.get(pk=request.user.pk) 
            return render(request, "index.html", {"mensaje": f'Datos actualizados!', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        
        avatar = Perfil.objects.get(pk=request.user.pk) 
        return render(request, "index.html", {"mensaje": 'Datos ingresados incorrectos', "url": avatar.Avatar.url, "banner":avatar.banner.url} )
    
    else:

        editform = PersonalFormulario(initial={"nombre":personal.nombre,
                                               "apellido":personal.apellido, 
                                               "dni":personal.dni, 
                                               "email":personal.email, 
                                               "telefono":personal.telefono, 
                                               "direccion":personal.direccion,})
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "Actualizar_PersonalCC.html", {"editform": editform, "url": avatar.Avatar.url, "banner":avatar.banner.url})      

def Borrar_PersonalCC(request, id):
    
    if request.method == 'POST':
    
        personalCC = PersonalCC.objects.get(id=id)
        personalCC.delete()
    
        personalCC = PersonalCC.objects.all()
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "index.html", {"mensaje":f'Personal borrado con exito', "url":avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Borrar_PersonalCC.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})

def Ver_PersonalCC(request, id):
    
    personalCC = PersonalCC.objects.get(id=id)
    avatar = Perfil.objects.get(pk=request.user.pk)
    
    return render(request, "Ver_PersonalCC.html", {"DetaileCC":personalCC, "url": avatar.Avatar.url, "banner":avatar.banner.url } )
       
def Listar_PersonalDXTV(request):
    
    personalDXTV = PersonalDXTV.objects.all()
    
    page = request.GET.get  ('page', 1)
    
    try:
        paginator=Paginator(personalDXTV, 8)
        personalDXTV =paginator.page(page)
        
    except:
       
        render(request, "Lista_Horas.html")
    
    avatar = Perfil.objects.get(pk=request.user.pk)
    return render(request, "Lista_PersonalDXTV.html", {"perDXTV":personalDXTV,
                                                       "page_obj" :personalDXTV,
                                                       "url":avatar.Avatar.url,
                                                       "banner":avatar.banner.url})
  
def editar_PersonalDXTV(request, id):
    
    personal = PersonalDXTV.objects.get(id=id)
    
    if request.method == 'POST':
            
        editform = PersonalFormulario(request.POST)

        if editform.is_valid():
           
            data = editform.cleaned_data
            
            personal.nombre=data["nombre"]
            personal.apellido=data["apellido"]
            personal.dni=data["dni"]
            personal.email=data["email"]
            personal.telefono=data["telefono"]
            personal.direccion=data["direccion"]         
            
            personal.save()
            
            avatar = Perfil.objects.get(pk=request.user.pk) 
            return render(request, "index.html", {"mensaje": f'Datos actualizados!', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        
        avatar = Perfil.objects.get(pk=request.user.pk) 
        return render(request, "index.html", {"mensaje": 'Datos ingresados incorrectos', "url": avatar.Avatar.url, "banner":avatar.banner.url} )
    
    else:

        editform = PersonalFormulario(initial={"nombre":personal.nombre,
                                               "apellido":personal.apellido, 
                                               "dni":personal.dni, 
                                               "email":personal.email, 
                                               "telefono":personal.telefono, 
                                               "direccion":personal.direccion,})
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "Actualizar_PersonalCC.html", {"editform": editform, "url": avatar.Avatar.url, "banner":avatar.banner.url})      

def Borrar_PersonalDXTV(request, id):
    
    if request.method == 'POST':
    
        personalDXTV = PersonalDXTV.objects.get(id=id)
        personalDXTV.delete()
    
        personalDXTV = PersonalDXTV.objects.all()
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "index.html", {"mensaje":f'Personal borrado con exito', "url":avatar.Avatar.url, "banner":avatar.banner.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Borrar_PersonalDXTV.html",{"url": avatar.Avatar.url, "banner":avatar.banner.url})

def Ver_PersonalDXTV(request, id):
    
    personalDXTV = PersonalDXTV.objects.get(id=id)
    avatar = Perfil.objects.get(pk=request.user.pk)
    
    return render(request, "Ver_PersonalDXTV.html", {"DetaileDXTV":personalDXTV, "url": avatar.Avatar.url, "banner":avatar.banner.url } )
       
    
    





