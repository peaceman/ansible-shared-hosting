Ansible Role: server_acmesh
===========================

Installs acme.sh and registers accounts for the staging and production environment

Requirements
------------

When using the acme dns-01 challenge, an aws access key is required.
Permissions needed described here: https://github.com/acmesh-official/acme.sh/wiki/How-to-use-Amazon-Route53-API

Role Variables
--------------

Defines

```
acme_config_base_path: /root/.config/acme
acme_path: /root/.acme.sh/acme.sh
acme_git_repo: https://github.com/Neilpang/acme.sh.git
acme_git_version: master

acme_account_email:
# used to access route53
acme_aws_access_key_id:
acme_aws_secret_access_key:
acme_base_alias_domain:
```

DNS-01 challenge
----------------

set cname

_acme-challenge.$domain -> $certName.$acmeBaseAliasDomain

Task Variables: certificate.yml
-------------------------------
# used as subdomain for the alias domain during dns-01 challenge
cert_name:
cert_domains: []

key_file_path:
csr_file_path:
cert_file_path:

# optional, if defined will be triggered from acme.sh after a certificate was updated
reload_cmd:

tls:
  source: self-signed # can be set to one of the following self-signed, acme, provided
  cert: # used when source is provided
  key: # used when source is provided
  acme:
    env: staging # one of production, staging
    challenge: dns-01 # one of dns-01, http-01
    force: false
