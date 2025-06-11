from django.urls import path

from app.views import *
from app.views_routes import *

urlpatterns = [
	path('', home, name = 'home'),
	
	# Routes
	
	path('view_route/<int:routeID>/', view_route, name = 'view_route'),
	path('view_routes/<int:Y>-<int:M>-<int:D>/', view_routes, name = 'view_routes'),
	
	path('route_creation/', route_creation, name = 'route_creation'),
	path('route_selection/', route_selection, name = 'route_selection'),
	
	# Other
	
	path('login/', login_view, name = 'login'),
	path('registrarse/', registrarse, name = 'registrarse'),
	
	path('reportes/', reportes, name = 'reportes'),
	path('crear_paquete/', crear_paquete, name = 'crear_paquete'),
	path('perfil', perfil, name='perfil'),
	path('logout', logout_view, name='logout'),
	
	path('envios/', envios, name = 'envios'),
	path('detalle_envios/<int:pk>/', detalle_envios, name = 'detalle_envios'),
    path('asignar_conductor', asignar_conductor, name='asignar_conductor')
]