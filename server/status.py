from datetime import datetime
import redis
from setup import settings


def get_user_status(user_id):
    redis_conn_pool_1 = settings.REDIS_CONN_POOL_1
    r = redis.Redis(connection_pool=redis_conn_pool_1)
    return r.exists(user_id) > 0


def mark_user_online(user_id):
    redis_conn_pool_1 = settings.REDIS_CONN_POOL_1
    r = redis.Redis(connection_pool=redis_conn_pool_1)
    now = datetime.now()
    r.setex(user_id, settings.KEY_TTL_IN_SECONDS, str(int(round(now.timestamp()))))
