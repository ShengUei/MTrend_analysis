import redis

from setting.connect_setting import get_redis_setting

def get_redis():
    return redis.Redis(
                        host = get_redis_setting().get('host'), 
                        port = get_redis_setting().get('port')
                        )