# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "education"
app_title = "Education"
app_publisher = "Frappe Technologies"
app_description = "ERP for Education"
app_icon = "octicon octicon-mortar-board"
app_color = "blue"
app_email = "info@frappe.io"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/education/css/education.css"
# app_include_js = "/assets/education/js/education.js"

# include js, css files in header of web template
# web_include_css = "/assets/education/css/education.css"
# web_include_js = "/assets/education/js/education.js"

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

# before_install = "education.install.before_install"
# after_install = "education.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "education.notifications.get_notification_config"

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
# 		"education.tasks.all"
# 	],
# 	"daily": [
# 		"education.tasks.daily"
# 	],
# 	"hourly": [
# 		"education.tasks.hourly"
# 	],
# 	"weekly": [
# 		"education.tasks.weekly"
# 	]
# 	"monthly": [
# 		"education.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "education.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "education.event.get_events"
# }

