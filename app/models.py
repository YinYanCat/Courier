from django.db import models

class Usuario(models.Model):
    ESTADO = [
        ('E', 'Enabled'),
        ('D', 'Disabled')
    ]

    nombre = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=50,default='')
    contraseña = models.CharField(max_length=128,default='')
    correo = models.EmailField(max_length=50,default='')
    telefono = models.CharField(max_length=50,default='')
    fecha_reg = models.DateField(auto_now_add=True)
    fecha_mod = models.DateField(auto_now=True)
    estado_usuario = models.CharField(max_length=1, choices=ESTADO, default='E')
    
    def __str__(self):
        return self.nombre

    class Meta():
        abstract = True

class Cliente(Usuario):
    pass
class Repartidor(Usuario):
    pass
class Administrador(Usuario):
    NIVEL_ACCESO = [
        ('T', 'Total')
    ]
    nivel_acceso = models.CharField(max_length=1, choices=NIVEL_ACCESO, default='T')
    ultimo_acceso = models.DateField(auto_now_add=False)


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

class Paquete(models.Model):
    usuario = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT, default=None, null=True)
    alto = models.FloatField()
    ancho = models.FloatField()
    largo = models.FloatField()
    peso = models.FloatField()
    dir_entrega = models.CharField(max_length=200, default=None)

    def __str__(self):
        return f"paquete {self.id} para {self.usuario.nombre}"

class Paquete_Estado(models.Model):
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE, related_name="historial_estados")
    estado = models.ForeignKey(Estado_entrega, on_delete=models.SET_NULL,null=True)
    fecha_hora = models.DateTimeField()

    def __str__(self):
        return f"{self.paquete} - {self.estado.nombre} ({self.fecha_hora})"

