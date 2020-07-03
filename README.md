# Ansible Collection - peaceman.shared_hosting

Collection of roles to provision a web shared hosting environment

## Sample Usage
Take a look at docs/sample folder for a single host example

## Dependencies
### Roles

```
# needed by common
- src: jnv.unattended-upgrades
  version: v1.8.0
# needed by server_mysql
- src: geerlingguy.mysql
  version: 3.1.0
```
