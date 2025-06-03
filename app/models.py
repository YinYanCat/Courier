from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    rut = models.CharField(max_length=16, unique=True)
    telefono = models.CharField(max_length=50,default='',null=True)
    fecha_mod = models.DateField(auto_now=True,null=True)

class Cliente(models.Model):
    ##is_staff deberia ser False siempre
    ##is_superuser deberia ser False siempre
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Administrador(models.Model):
    ##is_staff deberia ser True siempre
    ##is_superuser deberia ser False siempre
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

class Estado_entrega(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Ruta(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    distancia_km = models.FloatField()
    duracion_estimada = models.FloatField()

    def __str__(self):
        return f"{self.origen} → {self.destino}"

class Repartidor(models.Model):
    ##is_staff deberia ser False siempre
    ##is_superuser deberia ser False siempre
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.SET_NULL, null=True, blank=True)  

class Paquete(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ruta = models.ForeignKey(Ruta, on_delete=models.SET_NULL, null=True, blank=True)    
    alto = models.FloatField()
    ancho = models.FloatField()
    largo = models.FloatField()
    peso = models.FloatField()
    dir_entrega = models.CharField(max_length=200, default=None)

    def __str__(self):
        return f"paquete {self.id} para {self.cliente.nombre}"

class Paquete_Estado(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE, related_name="historial_estados")
    estado = models.ForeignKey(Estado_entrega, on_delete=models.SET_NULL,null=True)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.paquete} - {self.estado.nombre} ({self.fecha_hora})"

