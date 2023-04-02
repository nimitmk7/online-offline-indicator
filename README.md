# online-offline-indicator
Basic implementation of online-offline indicator server

Requirements: Redis cluster on local, Python VE to run the Django server.

**V0.1**

User's client has to send heartbeat signals to server, we store it in Redis as K-V pair, where key is user_id, value is timestamp of last heartbeat.
User is shown as online if the the timestamp retrieved by server from redis is less than 30 seconds from current timestamp(Server received a heartbeat in the last 30 seconds).

**V0.2**

We store the heartbeat K-V pair with a TTL of 60 seconds, which is now configurable from settings.py. To check whether client is online, server just checks 
the existence of key in Redis. Also introduced Redis connection pool.

