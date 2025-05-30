from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms.ClientForm import ClientForm
from app.factories.ClientFactory import ClientFactory

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def registro(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            factory = ClientFactory()
            try:
                factory.crear_usuario(rut=data['rut'], nombre=data['nombre'], apellido=data['apellido'], nombre_usuario=data['nombre_usuario'], contraseña=data['contraseña'], correo=data['correo'], telefono=data['telefono'])
                messages.success(request, 'Cliente creado con éxito')
                return redirect('registro')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
    else:
        form = ClientForm()
    return render(request, 'app/crear_cliente.html', {'form':form})

def login(request):
    return render(request, 'app/login.html')
def envios(request):
    return render(request, 'app/envios.html')