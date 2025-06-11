from app.models import Usuario, Cliente, DeliveryOrder, Warehouse, Route
from datetime import date
from app.utils.geocoding import ors_client

class OrderFactory:
	def __init__(self, usuario: Usuario):
		try:
			self.cliente = Cliente.objects.get(usuario=usuario)
		except Cliente.DoesNotExist:
			raise ValueError("Este usuario no está registrado como Cliente.")

	def crear_paquete(self, warehouse: Warehouse, alto, ancho, largo, peso, destino_str):
		lon, lat = ors_client.pelias_search(text=destino_str)['features'][0]['geometry']['coordinates']
		return DeliveryOrder.objects.create(
            client=self.cliente,
            warehouse=warehouse,
            destination_lat=lat,
            destination_lon=lon,
            dim_x=ancho,
            dim_y=alto,
            dim_z=largo,
            weight=peso
        )