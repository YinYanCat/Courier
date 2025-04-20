from django.urls import path
from .views import home, contactos, crear_usuario
urlpatterns = [
    path('', home, name='home'),
    path('contactos/', contactos, name='contactos'),
    path('crear_usuario/', crear_usuario, name='crear usuario')
]
