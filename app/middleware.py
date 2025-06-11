from django.db import connection

class SchemaMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response
	
	def __call__(self, request):
		connection.schema_name = 'courier'
		
		response = self.get_response(request)
		
		return response