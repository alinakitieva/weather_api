import requests
import json
from cache import get_cached_data, set_cached_data
from config import API_KEY, CACHE_EXPIRATION

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"


def fetch_weather(location, date1=None, date2=None):
    if date1 and date2:
        url = f"{BASE_URL}{location}/{date1}/{date2}?key={API_KEY}"
    elif date1:
        url = f"{BASE_URL}{location}/{date1}?key={API_KEY}"
    else:
        url = f"{BASE_URL}{location}?key={API_KEY}"

    cached_data = get_cached_data(url)
    if cached_data:
        return json.loads(cached_data)

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        set_cached_data(url, json.dumps(weather_data), CACHE_EXPIRATION)
        return weather_data
    else:
        response.raise_for_status()
