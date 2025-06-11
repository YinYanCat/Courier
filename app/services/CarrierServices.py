import folium
import openrouteservice

from openrouteservice import convert

from openrouteservice.optimization import Job
from openrouteservice.optimization import Vehicle
from app.utils.geocoding import ors_client
from ..repositories.CarrierRepository import CarrierRepository

SERVICE_TIME = 60

class CarrierServices:
	RouteManager = openrouteservice.Client(key = '5b3ce3597851110001cf62487b370cd078704024863ab1977ca4c5dc') # Remove key
	
	def createRoutes(SELF, date):
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
		
		routes = SELF.RouteManager.optimization(jobs = orsJobs, vehicles = orsTrucks, geometry = True)['routes']
		
		import json
		
		for routeData in routes:
			truckID = routeData['vehicle']
			
			route = CarrierRepository.createRoute(truckID = truckID, date = date, data = routeData)
			
			for step in routeData['steps']:
				if step['type'] == 'job':
					CarrierRepository.setRoute(step['job'], route.id)
		
		return
	
	def viewRoutesOn(SELF, date):
		warehouse = CarrierRepository.getWarehouses()[0]
		
		mapView = folium.Map(location = (warehouse.location_lat, warehouse.location_lon), zoom_start = 15, tiles = 'CartoDB Positron')
		
		routes = CarrierRepository.getRoutes(date = date)
		
		count = 0
		colors = ['red', 'green', 'blue']
		
		for route in routes:
			deliveries = CarrierRepository.getDeliveriesBy(routeID = route.id)
			
			for delivery in deliveries:
				folium.Marker(location = (delivery.destination_lat, delivery.destination_lon), icon = folium.Icon(color = colors[count % len(colors)])).add_to(mapView)
			
			routeLocations = []
			
			for location in convert.decode_polyline(route.data['geometry'])['coordinates']:
				routeLocations.append((location[1], location[0]))
			
			folium.PolyLine(locations = routeLocations, tooltip = f'Ruta {route.id}', color = colors[count % len(colors)], dashArray = 5).add_to(mapView)
			
			count += 1
		
		return mapView.get_root().render()