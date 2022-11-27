   

from django.urls import path




from .views import (

Crear_User_Admin,
Home,
Index,
edit_avatar,
 
editar_perfil,
loginview,
rigistrarse,
)

from django.contrib.auth.views import LogoutView
from .views import Index


urlpatterns =[
    path('', Home, name="Home"), 
    
    path('index/', Index, name="index"), 

    path('Login', loginview, name="login"),
    
    path('Editar_Perfil', editar_perfil, name="editarperfil"),
    
    path('Editar_Avatar', edit_avatar, name="EditarAvatar"),
    
    path('Crear_Admin', Crear_User_Admin, name="CrearAdmin"),
   
    path('Logout', LogoutView.as_view(template_name="Home.html"), name="logout"),
    
    
    
    
]