from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms.ClientForm import ClientForm
from app.factories.ClientFactory import ClientFactory

# Create your views here.

def home(request):
	return render(request, 'app/home.html')

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


def login(request):
	return render(request, 'app/login.html')
def envios(request):
	return render(request, 'app/envios.html')
def detalle_envios(request, pk):
	return render(request, 'app/detalle_envios.html', {'envio': pk})