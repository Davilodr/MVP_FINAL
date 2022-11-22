   

from django.urls import path


from .views import (

Index,
edit_avatar, 
editar_perfil,
loginview,
rigistrarse,
)

from django.contrib.auth.views import LogoutView
from .views import Index


urlpatterns =[
    path('', Index, name="index"), 

    path('Login', loginview, name="login"),
    
    path('Editar_Perfil', editar_perfil, name="editarperfil"),
   
    path('Logout', LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('Editar_Avatar', edit_avatar, name="EditarAvatar"),
    
    
    
]