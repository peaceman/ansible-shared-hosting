Ansible Role: server_php
=========

Installs php-fpm with multiple versions

Requirements
------------

Requires root access

Role Variables
--------------

Defines
```
php_versions:
  - 7.4
php_packages:
  - fpm
  - cli
  - ctype
  - curl
  - dom
  - iconv
  - gd
  - json
  - mbstring
  - simplexml
  - xml
  - zip
  - mysql
  - soap
  - fileinfo
  - intl
  - redis
  - apcu

php_post_max_size: 128M
php_upload_max_filesize: 128M
php_max_execution_time: 120
php_max_input_time: 120
php_memory_limit: 256M
php_opcache_memory_consumption: 512
php_opcache_validate_timestamps: 1
```

Uses
```
timezone: Europe/Berlin
nginx_user:
```

Dependencies
------------

Requires the server_nginx role to be ran before
