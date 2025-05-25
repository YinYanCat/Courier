from django.contrib import admin

# Register your models here.

from .models import Cliente, Repartidor, Administrador, Estado_entrega, Ruta, Paquete, Paquete_Estado

admin.site.register(Cliente)
admin.site.register(Repartidor)
admin.site.register(Administrador)

admin.site.register(Ruta)
admin.site.register(Paquete)
