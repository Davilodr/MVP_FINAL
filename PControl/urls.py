
from django.urls import path

from .views import (About, Borrar_PersonalCC, Borrar_PersonalDXTV, Borrar_dias, Buscar_datos, Buscar_dias,
                    Buscar_personalCC, Buscar_personalDXTV, BuscarD, BuscarP, 
                    Cargar_Personal, Crear_Datos, Crear_Hora,
                    Crear_User_PersonalCC, Crear_User_PersonalDXTV,
                    Crear_User_Supervisor, HorasList, Index,
                    Listar_Personal, Listar_dias, PersonalCCList, PersonalDXTVList, Update_PersonalCC, Update_PersonalDPTV,
                    Update_dias, Ver_PersonalCC, Ver_PersonalDXTV, crear_dias, editar_dias, filtrarD)

urlpatterns =[
    path('', Index, name="index"),
    
    path('Crear_dias/', crear_dias, name="CrearDias"),
    path('Lista_dias/', Listar_dias, name="ListaDias"),
    path('Actualizar_Dias/<int:id>', editar_dias, name="UpdateDias"),
    
    # path('Actualizar_Dias/<pk>', Update_dias.as_view(), name="UpdateDias"),
    path('Eliminar_Dias/<pk>', Borrar_dias.as_view(), name="BorrarDias"),
    path('Crear_Horas/', Crear_Hora.as_view(), name="CrearHoras"),
    path('Lista_Horas/', HorasList.as_view(), name="ListaHoras"),
    path('Lista_PersonalCC/', PersonalCCList.as_view(), name="ListaPersonalCC"),
    path('Lista_PersonalDXTV/', PersonalDXTVList.as_view(), name="ListaPersonalDXTV"),
    path('Ver_PersonalCC/<pk>', Ver_PersonalCC.as_view(), name="VerPersonalCC"),
    path('Ver_PersonalDXTV/<pk>', Ver_PersonalDXTV.as_view(), name="VerPersonalDXTV"),
    path('Actualizar_PCC/<pk>', Update_PersonalCC.as_view(), name="UpdatePersonalCC"),
    path('Actualizar_PDX/<pk>', Update_PersonalDPTV.as_view(), name="UpdatePersonalDXTV"),
    path('Eliminar_PersonalCC/<pk>', Borrar_PersonalCC.as_view(), name="BorrarPerCC"),
    path('Eliminar_PersonalDXTV/<pk>', Borrar_PersonalDXTV.as_view(), name="BorrarPerDXTV"),
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
    
    
  

]