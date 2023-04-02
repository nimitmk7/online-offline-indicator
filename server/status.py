from datetime import datetime
import redis
from setup import settings


def get_user_status(user_id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    last_heartbeat = r.get(user_id).decode()
    if int(last_heartbeat) < (datetime.now().timestamp() - 30):
        return "offline"
    return "online"


def mark_user_online(user_id):
    r = redis.Redis(host='localhost', port=6379, db=0)
    now = datetime.now()
    r.set(user_id, str(int(round(now.timestamp()))))
