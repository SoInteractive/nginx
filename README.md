<a href="https://www.nginx.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Nginx_logo.svg/2000px-Nginx_logo.svg.png" alt="nginx logo" title="nginx" align="right" height="60" />
</a>

Ansible Role: nginx
===================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/nginx/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fnginx/activity) [![License: MIT](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18219.svg)](https://galaxy.ansible.com/SoInteractive/nginx/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

This role will install and configure nginx and its sites. It supports SSL/TLS termination and letsencrypt autorenewal directory.

Disclaimer
----------

Ideas taken from https://github.com/jdauphant/ansible-role-nginx

Requirements
------------

When using metrics exporter, golang should be installed on deployer host. Also systemd is currently needed.

Examples
--------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.nginx
  
```

Whenever needed, you can pass `nginx_dh_remove_old=true` to ansible-playbook 
execution to remove previous Diffie-Hellman parameters

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
