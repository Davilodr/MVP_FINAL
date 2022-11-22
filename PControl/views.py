from django.shortcuts import render
from django.contrib.auth.models import Group



from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from Users.models import Perfil

from Users.form import PerfilUserCreationForm

from .form import Dias_Formulario, PersonalFormulario, UpdateDia_Form


from .models import Dias_trabajados, Horas_trabajadas, PersonalCC, PersonalDXTV, Supervisor
from django.views.generic import ListView

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User



def Index(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "index.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "index.html")
        
def Cargar_Personal(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Cargar_Personal.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "Cargar_Personal.html")
def About(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "About.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "About.html")
def Crear_Datos(request):
    try:  
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Crear_Datos.html",{"url": avatar.Avatar.url})
    except:
         return render(request, "Crear_Datos.html")
def Listar_Personal(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Lista_Personal.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "Lista_Personal.html")
def Buscar_datos(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_datos.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "Buscar_datos.html")
def Buscar_dias(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_dias.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "Buscar_dias.html")

def Buscar_personalCC(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalCC.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "Buscar_personalCC.html")
def Buscar_personalDXTV(request):
    try:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalDXTV.html",{"url": avatar.Avatar.url})
    except:
        return render(request, "Buscar_personalDXTV.html")


def BuscarP(request):
    
    if request.GET["dni"]:

        try:
            dni_buscada = request.GET["dni"]
            personal = PersonalCC.objects.get(dni=dni_buscada)
            avatar = Perfil.objects.get(pk=request.user.pk)

            return render(request, "Resultado_BuscarPCC.html", {"Personal": personal, "Dni": dni_buscada, "url": avatar.Avatar.url})
        except:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "Buscar_personalCC.html", {"mensaje": f'El dni ingresado no pertenece a Control Central', "url": avatar.Avatar.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalDXTV.html", {"mensaje": f'Los datos ingresados son incorrectos', "url": avatar.Avatar.url})

def BuscarD(request):
   
    
    if request.GET["dni"]:
        try:
            dni_buscada = request.GET["dni"]
            personal = PersonalDXTV.objects.get(dni=dni_buscada)
            avatar = Perfil.objects.get(pk=request.user.pk)
                   
            return render(request, "Resultado_BuscarPDX.html", {"Personal": personal, "Dni": dni_buscada, "url": avatar.Avatar.url})
        except:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "Buscar_personalDXTV.html", {"mensaje": f'El dni ingresado no pertenece a DXTV', "url": avatar.Avatar.url})
    else:
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Buscar_personalDXTV.html", {"mensaje": f'Los datos ingresados son incorrectos', "url": avatar.Avatar.url})
        

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
            return render(request, "index.html", {"mensaje": f'Perfil creado con exito', "url": avatar.Avatar.url})
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html",{"mensaje": f'Error, formulario invalido', "url": avatar.Avatar.url})      
    else:

        PersonalForm = PersonalFormulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        userform = PerfilUserCreationForm()

        return render(request, "personal_formularioCC.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url})

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
            return render(request, "index.html", {"mensaje": f'Perfil creado con exito', "url": avatar.Avatar.url})
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html",{"mensaje": f'Error, formulario invalido', "url": avatar.Avatar.url})
    else:

        PersonalForm = PersonalFormulario()
        avatar = Perfil.objects.get(pk=request.user.pk)
        userform = PerfilUserCreationForm()

        return render(request, "personal_formularioDXTV.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url})

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

        return render(request, "FormularioSupervisor.html", {"personalform": PersonalForm, "userform": userform, "url": avatar.Avatar.url})

def Listar_dias(request):
    
    diast = Dias_trabajados.objects.all()
    avatar = Perfil.objects.get(pk=request.user.pk)
    return render(request, "Lista_dias.html", {"diast":diast, "url":avatar.Avatar.url})


def filtrarD(request, id):
        
        nombreDT = Dias_trabajados.objects.filter(personal = id)
        
        nombreDT = nombreDT.values("personal")
        nombreDT = nombreDT.values()
        
                    
        return render(request, "diascc.html",{"diast":nombreDT})
    
def crear_dias(request):
    
    if request.method == 'POST':
        
        diasform= Dias_Formulario(request.POST)
        
        if diasform.is_valid():
            
            info = diasform.cleaned_data
            
            dia= Dias_trabajados(dia_trabajado=info['dia_trabajado'], personal=info['personal'])
            dia.save()
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render (request, "index.html", {"mensaje": f'Dia creado con exito',"url":avatar.Avatar.url})  
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html", {"mensaje": f'Datos ingresados invalidos',"url":avatar.Avatar.url})
    else:
        
        dias_form = Dias_Formulario
        avatar = Perfil.objects.get(pk=request.user.pk)
        return render(request, "Crear_dias.html", {"forms": dias_form, "url":avatar.Avatar.url})
  
    
def editar_dias(request, id):
    
    dia_trabajado = Dias_trabajados.objects.get(id=id)
    
    if request.method == 'POST':
            
        editform = UpdateDia_Form(request.POST)

        if editform.is_valid():
           
            data = editform.cleaned_data
            
            dia_trabajado.dia_trabajado = data["dia_trabajado"]
            dia_trabajado.personal = data["personal"]
            
            print(dia_trabajado)
        
            dia_trabajado.save()
            
            avatar = Perfil.objects.get(pk=request.user.pk) 
            return render(request, "index.html", {"mensaje": f'Datos actualizados!', "url": avatar.Avatar.url})
        
        avatar = Perfil.objects.get(pk=request.user.pk) 
        return render(request, "index.html", {"mensaje": 'Datos ingresados incorrectos', "url": avatar.Avatar.url} )
    
    else:

        editform = UpdateDia_Form(initial={"dia_trabajado":dia_trabajado.dia_trabajado, "personal":dia_trabajado.personal})
        avatar = Perfil.objects.get(pk=request.user.pk)            
        return render(request, "Actualizar_dias.html", {"editform": editform, "url": avatar.Avatar.url})     

    

class Update_dias(UpdateView):
    model = Dias_trabajados
    template_name = "Actualizar_dias.html"
    fields =('__all__')
    success_url = '/PControl/Lista_dias/'
 
    
class Borrar_dias(DeleteView):
    model = Dias_trabajados
    template_name = "Borrar_dias.html"
    fields =('__all__')
    success_url = '/PControl/Lista_dias/'
    
class HorasList(ListView):
    model = Horas_trabajadas
    template_name = 'Lista_Horas.html'
    context_object_name = "ListHoras"


class Crear_Hora(CreateView):
    model = Horas_trabajadas
    template_name = "Crear_Hora.html"
    fields =('__all__')
    success_url = '/PControl/Lista_Horas/'


class Update_Horas(UpdateView):
    model = Horas_trabajadas
    template_name = "Actualizar_Horas.html"
    fields =('__all__')
    success_url = '/PControl/Lista_Horas/'
    
    
class Borrar_Horas(DeleteView):
    model = Horas_trabajadas
    template_name = "Borrar_horas.html"
    fields =('__all__')
    success_url = '/PControl/Lista_Horas/'
    
class PersonalCCList(ListView):
    model = PersonalCC
    template_name = 'Lista_PersonalCC.html'
    context_object_name = "PerCC"
    
class Ver_PersonalCC(DetailView):
    model = PersonalCC
    template_name = "Ver_PersonalCC.html"
    context_object_name = "DetaileCC"

class Update_PersonalCC(UpdateView):
    model = PersonalCC
    template_name = "Actualizar_PersonalCC.html"
    fields =('__all__')
    success_url = '/PControl/Lista_PersonalCC/'

class Borrar_PersonalCC(DeleteView):
    model = PersonalCC
    template_name = "Borrar_PersonalCC.html"
    fields =('__all__')
    success_url = '/PControl/Lista_PersonalCC/'
    
class PersonalDXTVList(ListView):
    model = PersonalDXTV
    template_name = 'Lista_PersonalDXTV.html'
    context_object_name = "PerDXTV"
        
class Ver_PersonalDXTV(DetailView):
    model = PersonalDXTV
    template_name = "Ver_PersonalDXTV.html"
    context_object_name = "DetaileDXTV"

class Update_PersonalDPTV(UpdateView):
    model = PersonalDXTV
    template_name = "Actualizar_PersonalDXTV.html"
    fields =('__all__')
    success_url = '/PControl/Lista_PersonalDXTV/'

class Borrar_PersonalDXTV(DeleteView):
    model = PersonalDXTV
    template_name = "Borrar_PersonalDXTV.html"
    fields =('__all__')
    success_url = '/PControl/Lista_PersonalDXTV/'





