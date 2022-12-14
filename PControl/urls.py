
from django.urls import path
from Mensage.views import Crear_sugerencia, lista_sugerencia, ver_sugerencia

from Users.views import Cargar_personal_logout, Home, Sobre_Mi

from .views import (About,
                    Borrar_PersonalCC,
                    Borrar_PersonalDXTV,
                    Borrar_dias,
                    Borrar_horas,
                    Buscar_datos,
                    Buscar_dias,
                    Buscar_personalCC,
                    Buscar_personalDXTV,
                    BuscarD,
                    BuscarP, 
                    Cargar_Personal,
                    Crear_Datos,
                    Crear_User_PersonalCC,
                    Crear_User_PersonalDXTV,
                    Crear_User_Supervisor,
                    Facebook,
                    Github,
                    Gmail,
                    Index,
                    Listar_Personal,
                    Listar_PersonalCC,
                    Listar_PersonalDXTV,
                    Listar_dias,
                    Listar_horas, 
                    Telegram,
                    Ver_PersonalCC,
                    Ver_PersonalDXTV,
                    crear_dias,
                    crear_horas,
                    editar_PersonalCC,
                    editar_PersonalDXTV,
                    editar_dias,
                    editar_horas,
                    filtrarD,
                    filtrarH, 
                    linkedin)

urlpatterns =[
    path('', Home, name="Home"),
    path('Sobre_Mi/', Sobre_Mi, name="SobreMi"),
    path('Index/', Index, name="index"),
    path('Crear_dias/', crear_dias, name="CrearDias"),
    path('Lista_dias/', Listar_dias, name="ListaDias"),
    path('Actualizar_Dias/<int:id>', editar_dias, name="UpdateDias"),
    path('Eliminar_Dias/<int:id>', Borrar_dias, name="BorrarDias"),
    path('Crear_Horas/', crear_horas, name="CrearHoras"),
    path('Lista_Horas/', Listar_horas, name="ListaHoras"),
    path('Actualizar_Horas/<int:id>', editar_horas, name="UpdateHoras"),
    path('Eliminar_Horas/<int:id>', Borrar_horas, name="BorrarHoras"),
    path('Lista_PersonalCC/', Listar_PersonalCC, name="ListaPersonalCC"),
    path('Lista_PersonalDXTV/', Listar_PersonalDXTV, name="ListaPersonalDXTV"),
    path('Ver_PersonalCC/<int:id>', Ver_PersonalCC, name="VerPersonalCC"),
    path('Ver_PersonalDXTV/<int:id>', Ver_PersonalDXTV, name="VerPersonalDXTV"),
    path('Actualizar_PCC/<int:id>', editar_PersonalCC, name="UpdatePersonalCC"),
    path('Actualizar_PDX/<int:id>', editar_PersonalDXTV, name="UpdatePersonalDXTV"),
    path('Eliminar_PersonalCC/<int:id>', Borrar_PersonalCC, name="BorrarPerCC"),
    path('Eliminar_PersonalDXTV/<int:id>', Borrar_PersonalDXTV, name="BorrarPerDXTV"),
    path('Lista_Personal/', Listar_Personal, name="ListaPersonal"),
    path('Crear_Datos', Crear_Datos, name="CrearDatos"),
    path('Buscar_Datos', Buscar_datos, name="BuscarDatos"),
    path('Buscar_dias', Buscar_dias, name="BuscarDias"),
    path('Buscar_PersonalCC', Buscar_personalCC, name="BuscarPersonalCC"),
    path('Buscar_PersonalDXTV', Buscar_personalDXTV, name="BuscarPersonalDXTV"),
    path('BuscarP', BuscarP, name="BuscarP"),
    path('BuscarD', BuscarD, name="BuscarD"),
    path('Registrarse', Cargar_Personal, name="Registrar"),
    path('Crear_PersonalDXTV', Crear_User_PersonalDXTV, name="CreaPersonalDXTV"),
    path('Crear_PersonalCC', Crear_User_PersonalCC, name="CreaPersonalCC"),
    path('Crear_Supervisor', Crear_User_Supervisor, name="CreaSupervisor"),   
    path('Cargar_Personal', Cargar_Personal, name="CargarPersonalPage"),
    path('About', About, name="About"),
    path('Filtrar_dias/<int:id>', filtrarD, name="filtrarD"),
    path('Filtrar_horas/<int:id>', filtrarH, name="filtrarH"),
    path('Registrar_logout', Cargar_personal_logout, name="RegistrarLogout"),
    path('Facebook', Facebook, name="Facebook"),
    path('Gmail', Gmail, name="Gmail"),
    path('Github', Github, name="Github"),
    path('Linkedin', linkedin, name="Linkedin"),
    path('Telegram', Telegram, name="Telegram"),
    path('Sugerencia', Crear_sugerencia, name="Sugerencias"),
    path('Lista_sugerencia', lista_sugerencia, name="ListaSug"),
    path('Ver_Sugerencias/<int:id>', ver_sugerencia, name="VerSugerencia"),
]