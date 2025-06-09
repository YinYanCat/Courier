from django.contrib import admin

from .models import Usuario, Cliente, Administrador, Repartidor, Warehouse, Truck, Route, DeliveryOrder

admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Administrador)
admin.site.register(Repartidor)

admin.site.register(Warehouse)
admin.site.register(Truck)
admin.site.register(Route)
admin.site.register(DeliveryOrder)