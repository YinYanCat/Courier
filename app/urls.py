from django.urls import path
from .views import home, registro, login, envios, detalle_envios
urlpatterns = [
    path('', home, name='home'),
    path('crear_usuario/', registro, name='registro'),
    path('login/', login, name='login'),
    path('envios/',envios, name='envios'),
    path('detalle_envios/<int:pk>/', detalle_envios, name='detalle_envios')
]