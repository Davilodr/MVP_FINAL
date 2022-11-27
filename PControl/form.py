from django import forms

from .models import Dias_trabajados, Horas_trabajadas
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class Dias_Formulario(forms.ModelForm):

    class Meta:
        model = Dias_trabajados
        fields = ('__all__')
        widgets ={'dia_trabajado': DatePickerInput()}
        {'dia_trabajado': forms.TextInput(
                attrs={
                    'placeholder': "año-mes-dia",
                }
            )
        }



class UpdateDia_Form(forms.ModelForm):

    class Meta:
        model = Dias_trabajados
        fields = ('__all__')
        widgets ={
            'dia_trabajado': forms.TextInput(
                attrs={
                    'placeholder': "año-mes-dia",
                }
            )
        }

class Horas_Formulario(forms.ModelForm):

    class Meta:
        model = Horas_trabajadas
        fields = ('__all__')
        labels = {'personal1':('Personal'),}
        widgets ={
            'hora_trabajada': forms.TextInput(
                attrs={
                    'placeholder': "Igrese Horas",
                }
            )
        }
        
class Updatehoras_Form(forms.ModelForm):

    class Meta:
        model = Horas_trabajadas
        fields = ('__all__')
        labels = {'personal1':('Personal'),}
        widgets ={
            'hora_trabajada': forms.TextInput(
                attrs={
                    'placeholder': "Ingrese Horas",
                }
            )
        }
    
class PersonalFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    email = forms.EmailField(max_length=254)
    telefono= forms.IntegerField()
    direccion=forms.CharField(max_length=254)
    
    

        