from models import *
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

class CarrierServices:
	def __init__(self, repartidor:Repartidor):
		self.repartidor = repartidor

	def getNextRoute(self):
		return Ruta.object.filter(repartidor__isnull=true).first()

	def assignRoute(self,ruta:Ruta):
		repartidor.ruta = ruta
		repartidor.save()
		return ruta