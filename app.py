from flask import Flask
import json

from cache.redis_client import redis_client
from services.weather_services import get_weather
from config import CACHE_EXPIRY

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["50 per hour"]
)

@app.route("/weather/<city>")
@limiter.limit("10 per minute")
def weather(city):

    city = city.lower()

    cached_data = redis_client.get(city)

    if cached_data:
        return {
            "source": "cache",
            "data": json.loads(cached_data)
        }

    data = get_weather(city)

    redis_client.set(
        city,
        json.dumps(data),
        ex=CACHE_EXPIRY
    )

    return {
        "source": "api",
        "data": data
    }

if __name__ == "__main__":
    app.run(debug=True)