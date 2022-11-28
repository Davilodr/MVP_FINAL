

from django import forms

from Mensage.models import Sugerencia


class MensajeForm(forms.ModelForm):
    
    class Meta:
    
        model=Sugerencia
        fields=('nombre', 'mensaje')
        widgets ={'mensaje': forms.TextInput(
                attrs={
                    'placeholder': "Escriba su sugerencia aquí...",
                }
            )
        }
        {'nombre': forms.TextInput(
                attrs={
                    'placeholder': "Escriba su Nombre...",
                }
            )
        }