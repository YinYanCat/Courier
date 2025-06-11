from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from app.forms.ClientForm import ClientForm
from app.forms.OrderForm import OrderForm
from app.factories.ClientFactory import ClientFactory
from app.factories.OrderFactory import OrderFactory
from .models import Cliente, Administrador, Repartidor, Usuario, DeliveryOrder

def home(request):
	return render(request, 'app/home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('perfil')
        else:
            if not User.objects.filter(username=username).exists():
                messages.info(request, "El usuario no existe. Por favor, regístrate.")
                return redirect('registrarse')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
                return redirect('login')

    return render(request, 'app/login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def registrarse(request):
    if request.user.is_authenticated:
        logout(request)

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
def reportes(request):
    return render(request, 'app/reportes.html')
  
@login_required
def envios(request):
    usuario = request.user
    paquetes = []
    if hasattr(usuario, 'cliente'):
        try:
            cliente = Cliente.objects.get(usuario=usuario)
            paquetes = DeliveryOrder.objects.filter(client=cliente)
        except Cliente.DoesNotExist:
            pass
    if hasattr(usuario, 'repartidor'):
        try:
            repartidor = Repartidor.objects.get(usuario=usuario)
            paquetes = DeliveryOrder.objects.filter(route__truck__delivery_man=repartidor)
        except Repartidor.DoesNotExist:
            pass
    return render(request, 'app/envios.html', {'paquetes':paquetes})

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

@login_required
def perfil(request):
    usuario = request.user
    roles = []
    opciones = []

    if hasattr(usuario, 'cliente'):
        roles.append('Cliente')
        opciones.extend([
            {'nombre': 'Mis Envios', 'url': 'envios'},
            {'nombre': 'Crear Paquete', 'url': 'crear_paquete'}
        ])
    if hasattr(usuario, 'administrador'):
        roles.append('Administrador')
        opciones.extend([
            {'nombre': 'Reportes', 'url': 'reportes'},
            {'nombre': 'Crear Rutas', 'url': 'crear_rutas'},
            {'nombre': 'Ver Rutas', 'url': 'ver_rutas'},
            {'nombre': 'Asignar Conductores', 'url': 'home'} #cambiar
        ])
    if hasattr(usuario, 'repartidor'):
        roles.append('Repartidor')
        opciones.extend([
            {'nombre': 'Ver Envios Asignados', 'url': 'home'}, #cambiar
            {'nombre': 'Ver Mis Rutas', 'url': 'home'} #cambiar
        ])
    return render(request, 'app/profile.html', {
        'usuario': usuario,
        'roles': roles,
        'opciones': opciones
    })

@login_required
def asignar_conductor(request):
    usuario = request.user
    if hasattr(usuario, 'administrador'):
        pass
    else:
        return redirect('home')

@login_required
def mis_rutas(request):
    usuario = request.user
    if hasattr(usuario, 'repartidor'):
        pass
    else:
        return redirect('home')
