import os
import openrouteservice

from dotenv import load_dotenv

load_dotenv()

geoService = openrouteservice.Client(key = os.getenv('ORS_API_KEY', ''))