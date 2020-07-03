Ansible Role: server_borg
=========================

Installs and configures backups with borg onto a remote storage that is mounted via nfs or cifs

Downloads the repo key to borg-repo-keys/{{ ansible_host }}.txt

Role Variables
--------------

Defines
```
borg_remote_storage_type: # one of nfs, cifs
borg_remote_storage_address:
borg_remote_storage_username: # used with cifs
borg_remote_storage_password: # used with cifs
borg_remote_storage_mount_path: /mnt/backup-server # local path where the remote storage should be mounted to
borg_remote_storage_mount_options:
  cifs:
    - iocharset=utf8
    - rw
    - uid=root
    - gid=root
    - file_mode=0600
    - dir_mode=0750
    - noauto
    - vers=3
  nfs:
    - vers=4

borg_repo_path: repo # path below borg_remote_storage_mount_path to store the repo in
borg_passphrase: # passphrase that encrypts the repo key
borg_excludes: [] # additional paths that should not be included in the backup
borg_includes: [] # additional paths that should be included in the backup

borg_keep_daily: 7
borg_keep_weekly: 4
borg_keep_monthly: 6

borg_cron:
  minute: 23
  hour: 3
  day:
  weekday:
  month:
  special_time:

borg_additional_packages:
  cifs:
    - linux-generic
    - cifs-utils
  nfs:
    - nfs-client
```
