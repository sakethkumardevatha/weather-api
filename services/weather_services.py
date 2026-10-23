import requests

from config import WEATHER_API_KEY

def get_weather(city):
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"
    )
    params = {
        "unitGroup":"metric",
        "key":WEATHER_API_KEY,
        "contentType":"json"
    }
    response = requests.get(url,params=params)

    if response.status_code == 200:
        data = response.json()
        return {
        "city": data["resolvedAddress"],
        "temperature": data["currentConditions"]["temp"],
        "conditions": data["currentConditions"]["conditions"],
        "humidity": data["currentConditions"]["humidity"],
        "wind_speed": data["currentConditions"]["windspeed"]
    }
    else:
        return {"error": "Failed to fetch weather data"}    
    