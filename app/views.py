from app.forms.ClientForm import ClientForm
from app.factories.ClientFactory import ClientFactory
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Cliente, Administrador, Repartidor, Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if hasattr(user, 'administrador'):
                return redirect('reportes')
            elif hasattr(user, 'repartidor'):
                return redirect('detalle_envios')
            elif hasattr(user, 'cliente'):
                return redirect('envios')
            else:
                messages.error(request, "Tu cuenta no tiene un rol asignado.")
                return redirect('login')
        else:

            if not User.objects.filter(username=username).exists():
                messages.info(request, "El usuario no existe. Por favor, regístrate.")
                return redirect('registrarse')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
                return redirect('login')

    return render(request, 'app/login.html')


@login_required
def home(request):
    return render(request, 'app/home.html')

@login_required
def reportes(request):
    return render(request, 'app/reportes.html')

def registrarse(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            factory = ClientFactory()
            try:
                factory.crear_usuario(
                    rut=data['rut'],
                    nombre=data['nombre'],
                    apellido=data['apellido'],
                    nombre_usuario=data['nombre_usuario'],
                    contraseña=data['contraseña'],
                    correo=data['correo'],
                    telefono=data['telefono']
                )
                messages.success(request, 'Cliente creado con éxito. Ahora puedes iniciar sesión.')
                return redirect('login/')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = ClientForm()
    return render(request, 'app/registrarse.html', {'form': form})

@login_required
def envios(request):
    return render(request, 'app/envios.html')

@login_required
def detalle_envios(request, pk):
    return render(request, 'app/detalle_envios.html', {'envio': pk})
