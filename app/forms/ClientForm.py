from django import forms
from app.models import Usuario
from app.utils.Rut import checkRut, processRut

class ClientForm(forms.Form):
    rut = forms.CharField(max_length=16)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nombre_usuario = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=50, required=False)
    contraseña = forms.CharField(widget=forms.PasswordInput)
    repetir_contraseña = forms.CharField(widget=forms.PasswordInput)
    correo = forms.EmailField()

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        rut = processRut(rut)
        if not checkRut(rut):
            raise forms.ValidationError("RUT inválido.")
        return rut

    def clean_nombre_usuario(self):
        username = self.cleaned_data['nombre_usuario']
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_correo(self):
        email = self.cleaned_data['correo']
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("contraseña")
        repeat = cleaned_data.get("repetir_contraseña")
        if pwd and repeat and pwd != repeat:
            raise forms.ValidationError("Las contraseñas no coinciden.")