from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from Users.models import Perfil

class PerfilUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = Perfil
        fields =('username',)
        

        
class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    
    

    class Meta:

        model = Perfil
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2
    
class AvatarForm(UserChangeForm):
    
    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    
    class Meta:
        model=Perfil
        fields=('Avatar',)