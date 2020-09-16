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

systemd_services:
  - name:
    type: # service, timer, etc.
    enabled: true
    state: started
    template: # template path

ssh_keys:
  - key: https://github.com/peaceman.keys
    comment: peacemans key from github
```

System User Password Generation
-------------------------------

```
python3 -c "from passlib.hash import sha512_crypt; import getpass; print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))"
```

systemd Services
----------------

systemd services that will be managed by this role need to be configured, so that
they will always be restarted by systemd and don't run into the `StartLimitBurst` setting.

This is achievable for example by adding `StartLimitIntervalSec=0` to the unit section and
`RestartSec=5` to the service section.

The reason for this necessity is that the app_system role will almost always be executed
before all other app_* roles, which results in non existent binaries or scripts that systemd
will try to execute.
