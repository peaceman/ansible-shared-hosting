Ansible Role: app_nginx
=========

DNS-01 challenge
----------------

set cname

_acme-challenge.$domain -> $certGroupName.$acmeBaseAliasDomain

Requirements
------------

Requires a previously installed nginx service

Role Variables
--------------

Uses

```
username:
nginx_service: nginx
nginx_config_dir: /etc/nginx
acme_enabled: true
acme_config_base_path: /root/.config/acme
```

Defines

```
cert_groups:
  - name: # used as filename for the ssl certificate has to be server wide unique
    domains: []
    canonical_domain: # optional, has to be contained in domains to get a certificate
    wildcard_domain: # optional, if defined only a certificate for *.$wildcard_domain and $wildcard_domain will be generated
    tls:
      source: self-signed # can be set to one of the following self-signed, acme, provided
      cert: # used when source is provided
      key: # used when source is provided
      acme:
        env: staging # one of production, staging
        challenge: dns-01 # one of dns-01, http-01
        force: false

redirect_status_code: 301
document_root: # relative to the app folder, without leading slash
index_file: index.php
autoindex: "off"
charset: UTF-8
template: php-generic.conf.j2
configuration: []

ip_addresses: # optional, if defined will only listen on those addresses
  ipv4: []
  ipv6: []
```
