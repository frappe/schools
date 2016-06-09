# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "schools"
app_title = "ERPNext Schools"
app_publisher = "Frappe"
app_description = "ERP for Schools, Colleges and Other Acedemic Institutions"
app_icon = "octicon octicon-mortar-board"
app_color = "blue"
app_email = "hello@frappe.io"
app_license = "GNU General Public License v3"

# setup wizard
setup_wizard_requires = "assets/schools/js/setup_wizard.js"
setup_wizard_complete = "schools.setup_wizard.setup_complete"

required_apps = ["erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/schools/css/schools.css"
app_include_js = "/assets/js/schools.min.js"

# include js, css files in header of web template
# web_include_css = "/assets/schools/css/schools.css"
# web_include_js = "/assets/schools/js/schools.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]


# Installation
# ------------

# before_install = "schools.install.before_install"
# after_install = "schools.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "schools.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"schools.tasks.all"
# 	],
# 	"daily": [
# 		"schools.tasks.daily"
# 	],
# 	"hourly": [
# 		"schools.tasks.hourly"
# 	],
# 	"weekly": [
# 		"schools.tasks.weekly"
# 	]
# 	"monthly": [
# 		"schools.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "schools.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "schools.event.get_events"
# }

