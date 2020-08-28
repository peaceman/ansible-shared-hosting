Ansible Role: app_varnish
=========

Configures an app owned varnish instance

Requirements
------------

Requires an already installed varnish server

Role Variables
--------------

Uses
```
username:
# fill with name of template that should be used as base for the vcl e.g. shopware5.vcl.j2
varnish_vcl_template:
```

Defines
```
# defaults file for app_varnish
nginx_varnish_backend_ip: 127.0.0.23
nginx_varnish_backend_port: 80

# https://varnish-cache.org/docs/trunk/users-guide/storage-backends.html
varnish_storage_backend: malloc,256m
```
