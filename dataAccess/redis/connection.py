import redis

from setting.connect_setting import get_redis_setting

def get_redis():
    return redis.Redis(get_redis_setting())