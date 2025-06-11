from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	rut = models.CharField(max_length = 16, primary_key = True)
	telefono = models.CharField(max_length = 50, default = '')
	
	modification_date = models.DateTimeField(auto_now = True)

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
	location_lon = models.FloatField(default = None)
	location_lat = models.FloatField(default = None)

class Truck(models.Model):
	warehouse = models.ForeignKey(Warehouse, on_delete = models.PROTECT)
	
	capacity_x = models.FloatField()
	capacity_y = models.FloatField()
	capacity_z = models.FloatField()
	
	delivery_man = models.ForeignKey(Repartidor, on_delete = models.SET_NULL, null = True)

class Route(models.Model):
	truck = models.ForeignKey(Truck, on_delete = models.PROTECT)
	
	date = models.DateField()
	data = models.JSONField()

class DeliveryOrder(models.Model):
	class Status(models.IntegerChoices):
		AT_WAREHOUSE = 1
		IN_TRANSIT = 2
		DELIVERED = 3
	
	client = models.ForeignKey(Cliente, on_delete = models.PROTECT)
	warehouse = models.ForeignKey(Warehouse, on_delete = models.PROTECT)
	
	destination_lon = models.FloatField(default = None)
	destination_lat = models.FloatField(default = None)
	
	route = models.ForeignKey(Route, on_delete = models.SET_NULL, null = True)
	
	dim_x = models.FloatField()
	dim_y = models.FloatField()
	dim_z = models.FloatField()
	
	weight = models.FloatField()
	
	registration_date = models.DateField(auto_now_add = True)
	
	status = models.IntegerField(choices = Status, default = Status.AT_WAREHOUSE)