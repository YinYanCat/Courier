import folium

from openrouteservice import convert

from openrouteservice.optimization import Job
from openrouteservice.optimization import Vehicle

from app.utils.ors import geoService

from app.repositories.CarrierRepository import CarrierRepository

SERVICE_TIME = 60

class CarrierServices:
	@staticmethod
	def createRoutes(date):
		orsJobs = []
		orsTrucks = []
		
		warehouses = CarrierRepository.getWarehouses()
		
		for warehouse in warehouses:
			location = (warehouse.location_lon, warehouse.location_lat)
			
			trucks = CarrierRepository.getTrucks(warehouseID = warehouse.id)
			
			for truck in trucks:
				capacity = (truck.capacity_x, truck.capacity_y, truck.capacity_z)
				
				orsTrucks.append(Vehicle(truck.id, start = location, end = location, capacity = capacity))
			
			deliveries = CarrierRepository.getDeliveriesFrom(warehouseID = warehouse.id, amount = len(trucks))
			
			for delivery in deliveries:
				source = ()
				target = ()
				
				dims = (delivery.dim_x, delivery.dim_y, delivery.dim_z)
				
				orsJobs.append(Job(delivery.id, location = (delivery.destination_lon, delivery.destination_lat), service = SERVICE_TIME, amount = dims))
		
		routes = geoService.optimization(jobs = orsJobs, vehicles = orsTrucks, geometry = True)['routes']
		
		import json
		
		for routeData in routes:
			truckID = routeData['vehicle']
			
			route = CarrierRepository.createRoute(truckID = truckID, date = date, data = routeData)
			
			for step in routeData['steps']:
				if step['type'] == 'job':
					CarrierRepository.setRoute(step['job'], route.id)
		
		return
	
	@staticmethod
	def getRouteMap(routeID):
		route = CarrierRepository.getRoute(routeID = routeID)
		warehouse = route.truck.warehouse
		
		routeCoordinates = CarrierServices.__getRouteCoordinates(route)
		warehouseCoordinates = (warehouse.location_lat, warehouse.location_lon)
		
		mapView = folium.Map(location = warehouseCoordinates, zoom_start = 15, tiles = 'CartoDB Positron')
		
		for delivery in CarrierRepository.getDeliveriesBy(routeID = route.id):
			folium.Marker(location = (delivery.destination_lat, delivery.destination_lon), icon = folium.Icon(prefix = 'fa', icon = 'box-open', color = 'blue')).add_to(mapView)
		
		folium.Marker(location = warehouseCoordinates, icon = folium.Icon(prefix = 'fa', icon = 'house', color = 'orange')).add_to(mapView)
		folium.PolyLine(locations = routeCoordinates, color = 'blue', dashArray = 5).add_to(mapView)
		
		return mapView.get_root().render()
	
	@staticmethod
	def getRoutesMap(warehouseID, date):
		warehouse = CarrierRepository.getWarehouses()[0] # TEMP
		
		mapView = folium.Map(location = (warehouse.location_lat, warehouse.location_lon), zoom_start = 15, tiles = 'CartoDB Positron')
		
		routes = CarrierRepository.getRoutes(date = date)
		
		for route in routes:
			for delivery in CarrierRepository.getDeliveriesBy(routeID = route.id):
				folium.Marker(location = (delivery.destination_lat, delivery.destination_lon), icon = folium.Icon(prefix = 'fa', icon = 'box-open', color = 'blue')).add_to(mapView)
			
			routeCoordinates = CarrierServices.__getRouteCoordinates(route)
			
			folium.PolyLine(locations = routeCoordinates, tooltip = f'ID de ruta: {route.id}', color = 'blue', dashArray = 5).add_to(mapView)
		
		return mapView.get_root().render()
	
	@staticmethod
	def __getRouteCoordinates(route):
		coordinates = []
		
		for coordinate in convert.decode_polyline(route.data['geometry'])['coordinates']:
			coordinates.append((coordinate[1], coordinate[0]))
		
		return coordinates