Ansible Role: common
====================

* Install common packages
* Configures ssh
* Configures bash history
* Configures vim
* Sets timezone & hostname

Role Variables
--------------

Defines

```
sshd_config: /etc/ssh/sshd_config
sshd_service: ssh
timezone: Europe/Berlin
bashrc_config: /etc/bash.bashrc
unattended_origins_patterns:
  - 'origin=Ubuntu,archive=${distro_codename}-security'
  - 'o=Ubuntu,a=${distro_codename}'
  - 'o=Ubuntu,a=${distro_codename}-updates'
unattended_email: root
packages: []
mail_aliases_root: # mandatory
```
