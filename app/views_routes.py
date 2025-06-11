import datetime

from datetime import date

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from app.forms.RouteForm import RouteForm

from app.services.CarrierServices import CarrierServices

def view_route(request, routeID):
	mapView = CarrierServices.getRouteMap(routeID = routeID)
	
	return HttpResponse(mapView)

def view_routes(request, Y, M, D):
	mapView = CarrierServices.getRoutesMap(warehouseID = None, date = date(Y, M, D))
	
	return HttpResponse(mapView)

def route_selection(request):
	form = None
	mapView = None
	
	if request.method == 'POST':
		form = RouteForm(request.POST)
		
		if form.is_valid():
			data = form.cleaned_data
			date = data['date']
			
			mapView = f'/view_routes/{date}/'
	
	else:
		form = RouteForm()
		mapView = ""
	
	return render(request, 'app/route_selection.html', {'form': form, 'map': mapView})

def route_creation(request):
	tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
	
	CarrierServices.createRoutes(date = tomorrow)
	
	return redirect(f'/view_routes/{tomorrow}/')