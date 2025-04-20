from django.urls import path
from .views import home, contactos
urlpatterns = [
    path('', home, name='home'),
    path('contactos/', contactos, name='contactos'),
]
