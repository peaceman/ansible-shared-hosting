Sample Server Provisioning with the peaceman.shared_hosting Collection
======================================================================

Install dependencies
--------------------
    ansible-galaxy collection install -r requirements.yml
    ansible-galaxy role install -r requirements.yml

Provision
---------
ansible-playbook -i inventory $playbook.yml
