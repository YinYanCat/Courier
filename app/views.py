from django.http import HttpResponse
from app.forms.ClientForm import ClientForm
from app.forms.OrderForm import OrderForm
from app.factories.ClientFactory import ClientFactory
from app.factories.OrderFactory import OrderFactory
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Cliente, Administrador, Repartidor, Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .services.CarrierServices import CarrierServices

carrierServices = CarrierServices()

import datetime

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


def home(request):
    return render(request, 'app/home.html')

@login_required
def reportes(request):
    return render(request, 'app/reportes.html')

def ver_rutas(request):
	tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
	
	mapView = carrierServices.viewRoutesOn(date = tomorrow)
	
	return HttpResponse(mapView)

def crear_rutas(request):
	tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
	
	carrierServices.createRoutes(date = tomorrow)
	
	return redirect('ver_rutas')

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
                return redirect('login')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = ClientForm()
    return render(request, 'app/registrarse.html', {'form': form})

@login_required
def envios(request):
	return render(request, 'app/envios.html')


@login_required
def envios(request):
    return render(request, 'app/envios.html')

@login_required
def detalle_envios(request, pk):
    return render(request, 'app/detalle_envios.html', {'envio': pk})

@login_required
def crear_paquete(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            warehouse = form.cleaned_data['warehouse']
            destino = form.cleaned_data['destination']
            dim_x = form.cleaned_data['dim_x']
            dim_y = form.cleaned_data['dim_y']
            dim_z = form.cleaned_data['dim_z']
            peso = form.cleaned_data['weight']
            
            # Crear el paquete con coordenadas
            factory = OrderFactory(request.user)  # Asumiendo que Cliente hereda de User o está relacionado
            factory.crear_paquete(
                warehouse=warehouse,
                alto=dim_y,
                ancho=dim_x,
                largo=dim_z,
                peso=peso,
                destino_str=destino
            )
            messages.success(request, 'Paquete creado con éxito.')
            return redirect('crear_paquete')  # Cambia esto por la URL real de confirmación
    else:
        form = OrderForm()

    return render(request, 'app/crear_paquete.html', {'form': form})

def nuevo_paquete(request):
    if request.method == 'POST':
        #cliente = request.POST.get('cliente')
        #ruta = request.POST.get('ruta')
        #alto = request.POST.get('alto')
        #ancho = request.POST.get('ancho')
        #largo = request.POST.get('largo')
        #peso = request.POST.get('peso')
        #dir_entrega = request.POST.get('dir_entrega')

        # TODO: Validar los datos del formulario
        messages.success(request, 'Paquete creado con éxito.')
        return redirect('envios')
    return render(request, 'app/crear_paquete.html')