Ansible Role: server_nginx
=========

Installs and configures nginx with brotli support

Requirements
------------

Requires root access

When using the acme dns-01 challenge, an aws access key is required.
Permissions needed described here: https://github.com/acmesh-official/acme.sh/wiki/How-to-use-Amazon-Route53-API

Role Variables
--------------

Defines

```
nginx_service: nginx
nginx_user: nginx
nginx_ssl_dhparam_size: 4096
nginx_config_dir: /etc/nginx

acme_path: /root/.acme.sh/acme.sh
acme_account_email:
acme_config_base_path: /root/.config/acme
acme_git_repo: https://github.com/Neilpang/acme.sh.git
acme_git_version: master
acme_base_alias_domain:

# used to access route53
acme_aws_access_key_id:
acme_aws_secret_access_key:

```
