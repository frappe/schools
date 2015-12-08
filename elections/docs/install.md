<!-- title: Frappe Schools Installation -->

# Installation

Frappe Schools is based on the <a href="https://frappe.io">Frappe Framework</a>, a full stack web framework based on Python, MariaDB, Redis, Node.

To intall Frappe Schools, you will have to install the <a href="https://github.com/frappe/bench">Frappe Bench</a>, the command-line, package manager and site manager for Frappe Framework. For more details, read the Bench README.

After you have installed Frappe Bench, go to you bench folder, which is     `frappe.bench` by default and setup **schools**.

    bench get-app schools {{ source_link }}

Then create a new site to install the app.

    bench new-site mysite

This will create a new folder in your `/sites` directory and create a new database for this site.

Next, install schools in this site

    bench --site mysite install-app schools

To run this locally, run

    bench start

Fire up your browser and go to http://localhost:8000 and you should see the login screen. Login as **Administrator** and **admin** (or the password you set at the time of `new-site`) and you are set.

<!-- jinja -->
<!-- autodoc -->