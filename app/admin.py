from django.contrib import admin

# Register your models here.

from .models import Usuario, Estado_entrega, Ruta, Paquete, Paquete_Estado

admin.site.register(Usuario)
admin.site.register(Estado_entrega)
admin.site.register(Ruta)
admin.site.register(Paquete)
admin.site.register(Paquete_Estado)