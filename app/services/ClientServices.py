from models import Cliente, DeliveryOrder
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

class ClientServices:
	def __init__(self, cliente:Cliente):
		if not isinstance(cliente, Cliente):
			raise PermissionDenied("El usuario no es cliente")
		
		self.cliente = cliente

	def getOrders(self):
		return DeliveryOrder.objects.filter(usuario=self.cliente)
	
	def getOrder(self, paquete_id):
		try:
			return DeliveryOrder.objects.get(id=paquete_id, cliente=self.cliente)
		
		except ObjectDoesNotExist:
			return None