import requests
import json
from cache import get_cached_data, set_cached_data
from config import Config
import logging

logger = logging.getLogger(__name__)

BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"


def fetch_weather(location, date1=None, date2=None):
    if date1 and date2:
        url = f"{BASE_URL}{location}/{date1}/{date2}?key={Config.API_KEY}"
    elif date1:
        url = f"{BASE_URL}{location}/{date1}?key={Config.API_KEY}"
    else:
        url = f"{BASE_URL}{location}?key={Config.API_KEY}"

    logger.info(f"Fetching weather data for URL: {url}")

    cached_data = get_cached_data(url)
    if cached_data:
        logger.info(f"Returning cached weather data for {location}")
        return json.loads(cached_data)

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        set_cached_data(url, json.dumps(weather_data), Config.CACHE_EXPIRATION)
        logger.info(f"Fetched and cached weather data for {location}")
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {str(http_err)}")
        raise
    except Exception as err:
        logger.error(f"Other error occurred: {str(err)}")
        raise
