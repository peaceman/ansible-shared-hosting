Ansible Role: server_nginx
=========

Installs and configures nginx with brotli support

Requirements
------------

Requires root access

Role Variables
--------------

Uses

```
# if enabled install acmesh and creates nginx vhost snippets for acmesh stateless auth
acme_enabled: true
acme_config_base_path: /root/.config/acme
```

Defines

```
nginx_service: nginx
nginx_user: nginx
nginx_ssl_dhparam_enable: true
nginx_ssl_dhparam_size: 4096
nginx_config_dir: /etc/nginx
```
