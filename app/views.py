from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')
def registro(request):
    return render(request, 'app/crear_usuario.html')
def login(request):
    return render(request, 'app/login.html')
def envios(request):
    return render(request, 'app/envios.html')
def detalle_envios(request, pk):
    return render(request, 'app/detalle_envios.html', {'envio': pk})