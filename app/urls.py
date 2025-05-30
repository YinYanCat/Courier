from django.urls import path
from .views import home, registro, login, envios
urlpatterns = [
    path('', home, name='home'),
    path('crear_cliente/', registro, name='registro'),
    path('login/', login, name='login'),
    path('envios/',envios, name='envios')
]
