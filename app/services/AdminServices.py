from app.models import Administrador, DeliveryOrder, Repartidor, Truck
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

class AdminServices:

    def setTruckDriver(self, truck_id, carrier_id):
        try:
            truck = Truck.objects.get(id=truck_id)
        except Truck.DoesNotExist:
            raise ObjectDoesNotExist("Camión no encontrado.")
        if carrier_id == 'none':
            truck.delivery_man = None
        else:
            try:
                carrier = Repartidor.objects.get(id=carrier_id)
                truck.delivery_man = carrier
            except Repartidor.DoesNotExist:
                raise ObjectDoesNotExist("Repartidor no encontrado.")
        truck.save()
        