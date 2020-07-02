Ansible Role app_php
=========

Configures a php fpm pool for the given user

Requirements
------------

Requires an installed php-fpm service

Role Variables
--------------

Uses

```
nginx_user:
username:
```

Defines

```
php_version:

pm_mode: dynamic
pm_max_children: 10
pm_start_servers: 5
pm_min_spare_servers: 3
pm_process_idle_timeout: 10s

fpm_directives: []
```
