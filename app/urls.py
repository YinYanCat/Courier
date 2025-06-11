from django.urls import path

from .views import home, ver_rutas, crear_rutas, registrarse, envios, detalle_envios, login_view, reportes, crear_paquete

urlpatterns = [
	path('', home, name='home'),
	
	path('ver_rutas/', ver_rutas, name = 'ver_rutas'),
	path('crear_rutas/', crear_rutas, name = 'crear_rutas'),
	
	path('login/', login_view, name = 'login'),
	path('registrarse/', registrarse, name = 'registrarse'),
	
	path('envios/', envios, name='envios'),
	path('detalle_envios/<int:pk>/', detalle_envios, name = 'detalle_envios'),
  	path('reportes/', reportes, name = 'reportes'),
  	path('crear_paquete/', crear_paquete, name = 'crear_paquete'),
]