from app.models import Warehouse
from app.models import Truck
from app.models import Route
from app.models import DeliveryOrder

class CarrierRepository:
	@staticmethod
	def getWarehouses():
		return Warehouse.objects.all()
	
	@staticmethod
	def getTrucks(warehouseID):
		return Truck.objects.filter(warehouse_id = warehouseID)
	
	@staticmethod
	def getDeliveriesBy(routeID):
		return DeliveryOrder.objects.filter(route_id = routeID)
	
	@staticmethod
	def getDeliveriesFrom(warehouseID, amount):
		return DeliveryOrder.objects.filter(warehouse_id = warehouseID, route_id = None)[0 : amount]
	
	@staticmethod
	def getRoute(routeID):
		return Route.objects.get(id = routeID)
	
	@staticmethod
	def getRoutes(date):
		return Route.objects.filter(date = date)
	
	@staticmethod
	def setRoute(deliveryID, routeID):
		delivery = DeliveryOrder.objects.get(id = deliveryID)
		
		delivery.route_id = routeID
		
		delivery.save()
	
	@staticmethod
	def createRoute(truckID, date, data):
		route = Route(date = date, data = data, truck_id = truckID)
		
		route.save()
		
		return route