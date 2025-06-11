from django.conf import settings
from openrouteservice import Client

ors_client = Client(key=settings.OPENROUTESERVICE_API_KEY)