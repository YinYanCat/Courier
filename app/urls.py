from django.urls import path

from .views import home, ver_rutas, crear_rutas, login, registrarse, envios, detalle_envios

urlpatterns = [
	path('', home, name = 'home'),
	
	path('ver_rutas/', ver_rutas, name = 'ver_rutas'),
	path('crear_rutas/', crear_rutas, name = 'crear_rutas'),
	
	path('login/', login, name = 'login'),
	path('registrarse/', registrarse, name = 'registrarse'),
	
	path('envios/', envios, name = 'envios'),
	path('detalle_envios/<int:pk>/', detalle_envios, name = 'detalle_envios')
]