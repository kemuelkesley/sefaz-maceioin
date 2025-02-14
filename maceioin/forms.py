from django import forms
from .models import  Servidor


# class UsuarioForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['username', 'password']

class ServidorForm(forms.ModelForm):
    class Meta:
        model = Servidor
        fields = ['nome', 'setor', 'email']
        
                
