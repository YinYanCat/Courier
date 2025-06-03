from django.contrib.auth.models import Cliente, Paquete
from datetime import date

class PaqueteFactory:
	def __init__(self, cliente: Cliente):
		self.cliente = cliente

	def crear_paquete(self, descripcion, alto, ancho, largo, peso, dir_entrega):
		return Paquete.objects.create(
			cliente=self.cliente,
			descripcion=descripcion,
			alto=alto,
			ancho=ancho,
			largo=largo,
			peso=peso,
			dir_entrega=dir_entrega,
			fecha_envio=date.today()
		)