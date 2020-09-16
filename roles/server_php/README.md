Ansible Role: server_php
=========

Installs php-fpm with multiple versions

Requirements
------------

Requires root access

Role Variables
--------------

Defines
```yaml
php_versions:
  - 7.4
php_packages: [] # packages to install additionaly to the default  ones
php_version_packages: # packages to install additionaly for the specified php version
  "7.4": []

php_post_max_size: 128M
php_upload_max_filesize: 128M
php_max_execution_time: 120
php_max_input_time: 120
php_memory_limit: 256M
php_opcache_memory_consumption: 512
php_opcache_validate_timestamps: 1
```

Uses
```yaml
timezone: Europe/Berlin
nginx_user:
```

Used by task file install_php_extension.yml
```yaml
php_version:
# full path to the extension so
extension_file:
ini_filename:
ini_content:
```

Dependencies
------------

Requires the server_nginx role to be ran before
