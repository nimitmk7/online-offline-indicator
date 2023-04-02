# online-offline-indicator
Basic implementation of online-offline indicator server

Requirements: Redis cluster on local, Python VE to run the Django server.

**V0.1**

User's client has to send heartbeat signals to server, we store it in Redis as K-V pair, where key is user_id, value is timestamp of last heartbeat.
User is shown as online if the the server has received a heartbeat in the last 30 seconds. 


