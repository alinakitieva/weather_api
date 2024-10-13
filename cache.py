import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_DB

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)


def get_cached_data(key):
    return redis_client.get(key)


def set_cached_data(key, value, expiration):
    redis_client.set(key, value, ex=expiration)
