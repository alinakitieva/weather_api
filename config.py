import os
import logging

class Config:
    API_KEY = os.getenv("WEATHER_API_KEY")
    REDIS_HOST = "localhost"
    REDIS_PORT = 6379
    REDIS_DB = 0
    CACHE_EXPIRATION = 43200  # 12 hours
    RATE_LIMIT = 100  # 100 requests per hour
    LOG_LEVEL = logging.DEBUG if os.getenv("FLASK_ENV") == "development" else logging.INFO
    LOG_FILE = "app.log"
