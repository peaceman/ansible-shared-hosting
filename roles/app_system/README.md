Ansible Role: app_system
=========

Creates the applications system user and some configuration files

Requirements
------------

Requires root access

Role Variables
--------------

Uses
```
username:
nginx_user:
mysql_username:
mysql_password:
mysql_host:
crons:
  - name: check php version
    job: php -v >> logs/php-version.txt
    minute:
    hour:
    day:
    weekday:
    month:
    special_time:
```
