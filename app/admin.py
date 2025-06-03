from django.contrib import admin

# Register your models here.

from .models import Usuario, Cliente, Repartidor, Administrador, Estado_entrega, Ruta, Paquete, Paquete_Estado

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Repartidor)
admin.site.register(Administrador)

admin.site.register(Ruta)
admin.site.register(Paquete)
admin.site.register(Paquete_Estado)
