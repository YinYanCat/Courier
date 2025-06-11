from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	rut = models.CharField(max_length = 16, primary_key = True)
	telefono = models.CharField(max_length = 50, default = '', null = True)
	
	modification_date = models.DateTimeField(auto_now = True, null = False)

class Cliente(models.Model):
	"""
		* is_staff deberia ser False siempre
		* is_superuser deberia ser False siempre
	"""
	
	usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)

class Administrador(models.Model):
	"""
		* is_staff deberia ser True siempre
		* is_superuser deberia ser False siempre
	"""
	
	usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)

class Repartidor(models.Model):
	"""
		* is_staff deberia ser False siempre
		* is_superuser deberia ser False siempre
	"""
	
	usuario = models.OneToOneField(Usuario, on_delete = models.CASCADE)

class Warehouse(models.Model):
	location_lon = models.FloatField(default = None, null = False)
	location_lat = models.FloatField(default = None, null = False)

class Truck(models.Model):
	warehouse = models.ForeignKey(Warehouse, on_delete = models.PROTECT, null = False)
	
	capacity_x = models.FloatField(null = False)
	capacity_y = models.FloatField(null = False)
	capacity_z = models.FloatField(null = False)
	
	delivery_man = models.ForeignKey(Repartidor, on_delete = models.SET_NULL, null = True)

class Route(models.Model):
	truck = models.ForeignKey(Truck, on_delete = models.PROTECT, null = False)
	
	date = models.DateField(null = False)
	data = models.JSONField()

class DeliveryOrder(models.Model):
	client = models.ForeignKey(Cliente, on_delete = models.PROTECT, null = False)
	warehouse = models.ForeignKey(Warehouse, on_delete = models.PROTECT, null = False)
	
	destination_lon = models.FloatField(default = None, null = False)
	destination_lat = models.FloatField(default = None, null = False)
	
	route = models.ForeignKey(Route, on_delete = models.SET_NULL, null = True)
	
	dim_x = models.FloatField(null = False)
	dim_y = models.FloatField(null = False)
	dim_z = models.FloatField(null = False)
	
	weight = models.FloatField(null = False, blank = False)
	
	registration_date = models.DateField(auto_now_add = True, null = False)