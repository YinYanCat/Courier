from django import forms

class ClientForm(forms.Form):
    rut = forms.CharField(max_length=16)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nombre_usuario = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=50, required=False)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    correo = forms.EmailField()
