
from django.shortcuts import render
from Users.models import Perfil
from Mensage.models import Sugerencia


from django.core.paginator import Paginator

# Create your views here.

def Crear_sugerencia(request):
    
    if request.method == 'POST':
        
        nombre = Perfil.objects.get(username = request.user)
        
        
        if nombre == request.user:
            
            
            info= request.POST
            
            if nombre == info['nombre']:
                
                if info['texto']:
                
                    form={"nombre":info['nombre'],
                    "mensaje":info['texto']}
                
                    data= Sugerencia(nombre = form['nombre'], mensaje = form['mensaje'], mensaje_id=request.user)
                
                    data.save()
                    avatar = Perfil.objects.get(pk=request.user.pk)
                    return render(request, "index.html",{"mensaje":f'Sugerencia enviada con éxito', "url": avatar.Avatar.url, "banner":avatar.banner.url})
                else:
                    avatar = Perfil.objects.get(pk=request.user.pk)
                    return render(request, "index.html",{"mensaje":f'Debe ingresar Sugerencia', "url": avatar.Avatar.url, "banner":avatar.banner.url})
            
            else:
                avatar = Perfil.objects.get(pk=request.user.pk)
                return render(request, "index.html",{"mensaje":f'Nombre de usuario no valido', "url": avatar.Avatar.url, "banner":avatar.banner.url})
        else:
            avatar = Perfil.objects.get(pk=request.user.pk)
            return render(request, "index.html",{"mensaje":f'Debe ingresar su nombre de usuario', "url": avatar.Avatar.url, "banner":avatar.banner.url})
    
    
def lista_sugerencia(request):
    
    mensaje = Sugerencia.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator=Paginator(mensaje, 5)
        mensaje =paginator.page(page)
        
    except:
        render(request, "index.html")
    
    avatar = Perfil.objects.get(pk=request.user.pk)
    return render(request, "Lista_sugerencia.html", {"msjs":mensaje, "page_obj":mensaje, "url":avatar.Avatar.url, "banner":avatar.banner.url})   
        
def ver_sugerencia(request, id):
    
    mensaje = Sugerencia.objects.get(id=id)
    avatar = Perfil.objects.get(pk=request.user.pk)
    
    return render(request, "Ver_Sugerencia.html", {"msj":mensaje, "url": avatar.Avatar.url, "banner":avatar.banner.url } )