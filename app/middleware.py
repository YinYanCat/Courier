from django.db import connection

class SchemaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Establecer el esquema para todas las consultas
        connection.schema_name = 'courier'  

        print(f"Middleware está usando el esquema: {connection.schema_name}")

        response = self.get_response(request)
        return response