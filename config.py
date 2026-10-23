import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

REDIS_URL = os.getenv("REDIS_URL")

CACHE_EXPIRY = int(os.getenv("CACHE_EXPIRY", 43200))