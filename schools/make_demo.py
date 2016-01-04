# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe, os
from frappe.core.page.data_import_tool.data_import_tool import import_doc
from schools.simulate import simulate

def make():
	frappe.flags.mute_emails = True
	setup()
	frappe.set_user("Administrator")

def setup():
	complete_setup()
	make_masters()
	make_student_applicants()
	simulate()
	
def complete_setup():
	print "Complete Setup..."
	from frappe.desk.page.setup_wizard.setup_wizard import setup_complete
	setup_complete({
		"first_name": "Demo",
		"last_name": "User",
		"email": "demo@erpnext.com",
		"company_tagline": "Inspiring Minds",
		"password": "demo",
		"fy_start_date": "2015-01-01",
		"fy_end_date": "2015-12-31",
		"industry": "Education",
		"company_name": "Whitemore College",
		"chart_of_accounts": "Standard",
		"company_abbr": "WC",
		"country": "United States",
		"currency": "USD",
		"timezone": "America/New_York",
		"bank_name": "Citibank",
		"language": "english"
	})

	# home page should always be "start"
	website_settings = frappe.get_doc("Website Settings", "Website Settings")
	website_settings.home_page = "start"
	website_settings.save()

	frappe.clear_cache()
	
def make_masters():
	import_data("Room")
	import_data("Department")
	import_data("Instructor")
	import_data("Course")
	import_data("Program")
	
def make_student_applicants():
	import_data("Student Applicant")

def import_data(dt, submit=False, overwrite=False):
	if not isinstance(dt, (tuple, list)):
		dt = [dt]

	for doctype in dt:		
		import_doc(get_json_path(doctype), submit=submit, overwrite=overwrite)
		
def get_json_path(doctype):
	return os.path.join(os.path.dirname(__file__), "demo_docs", doctype+".json")