import redis
from config import Config
import logging

logger = logging.getLogger(__name__)

redis_client = redis.Redis(
    host=Config.REDIS_HOST, port=Config.REDIS_PORT, db=Config.REDIS_DB
)


def get_cached_data(key):
    try:
        data = redis_client.get(key)
        if data:
            logger.info(f"Cache hit for key: {key}")
        else:
            logger.info(f"Cache miss for key: {key}")
        return data
    except redis.RedisError as e:
        logger.error(f"Error accessing Redis: {str(e)}")
        return None


def set_cached_data(key, value, expiration):
    redis_client.set(key, value, ex=expiration)
