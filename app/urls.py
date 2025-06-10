from django.urls import path
from .views import home, registrarse, login_view, envios, detalle_envios, reportes

urlpatterns = [
    path('', home, name='home'),
    path('registrarse/', registrarse, name='registrarse'),
    path('login/', login_view, name='login'),
    path('envios/', envios, name='envios'),
    path('detalle_envios/<int:pk>/', detalle_envios, name='detalle_envios'),
    path('reportes/', reportes, name='reportes'),

]
