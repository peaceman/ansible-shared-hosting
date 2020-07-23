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
password: # optional
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

ssh_keys:
  - key: https://github.com/peaceman.keys
    comment: peacemans key from github
```

System User Password Generation
-------------------------------

```
python3 -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))"
```
