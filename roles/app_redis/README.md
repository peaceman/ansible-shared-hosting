Ansible Role: app_redis
=========

Configures an app owned redis instance

Requirements
------------

Requires an already installed redis-server

Role Variables
--------------

Uses
```
username:
```

Defines
```
socket_filename: redis.sock
log_filename: redis.log
config_filename: redis.conf
service_name: redis
maxmemory: 256mb
maxmemory_policy: volatile-lru
redis_server_binary: /usr/bin/redis-server
```
