#ERP for Schools, Colleges & Educational Institutes
[![Build Status](https://travis-ci.org/frappe/schools.png)](https://travis-ci.org/frappe/schools) [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/frappe/erpnext?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
---
Frappé Schools is built on the [Frappé](https://github.com/frappe/frappe) Framework, a full-stack web app framework in Python & JavaScript.

Requires [EPRNext](https://github.com/frappe/erpnext), 

Read the User and Developer Documentation at https://frappe.github.io/schools

![candidate](schools/public/candidate.png)

### Full Install

The Easy Way: our install script for bench will install all dependencies (e.g. MariaDB). See https://github.com/frappe/bench for more details.

New passwords will be created for the ERPNext "Administrator" user, the MariaDB root user, and the frappe user (the script displays the passwords and saves them to ~/frappe_passwords.txt).

Once you install ERPNext run -

```
$ bench get-app schools https://github.com/frappe/schools
$ bench install-app schools
```

#### License
GNU General Public License v3

The Frappe Schools code is licensed as GNU General Public License (v3) and the Documentation is licensed as Creative Commons (CC-BY-SA-3.0) and the copyright is owned by Frappe Technologies 