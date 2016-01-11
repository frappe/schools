# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe, os, json
from frappe.core.page.data_import_tool.data_import_tool import import_doc
from schools.simulate import simulate
from frappe.utils.make_random import get_random
import time

def make():
	frappe.flags.mute_emails = True
	setup()
	frappe.set_user("Administrator")

def setup():
	print "Completing Setup..."
	complete_setup()
	print "Making Masters..."
	make_masters()
	make_student_applicants()
	make_student_group()
	print "Starting Simulation..."
	time.sleep(5)
	simulate()
	
def complete_setup():
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
	file_path = get_json_path("Random Student Data")
	with open(file_path, "r") as open_file:
		random_student_data = json.loads(open_file.read())
		for d in random_student_data:
			student_applicant = frappe.new_doc("Student Applicant")
			student_applicant.first_name = d.get('first_name').title()
			student_applicant.last_name = d.get('last_name').title()
			student_applicant.image = d.get('image')
			student_applicant.gender = d.get('gender')
			student_applicant.program = get_random("Program")
			student_applicant.submit()

def make_student_group():
	for d in frappe.db.get_list("Academic Term"):
		sg_tool = frappe.new_doc("Student Group Creation Tool")
		sg_tool.academic_year = "2016-17"
		sg_tool.academic_term = d.name
		sg_tool.courses = sg_tool.get_courses()
		sg_tool.create_student_groups()

def import_data(dt, submit=False, overwrite=False):
	if not isinstance(dt, (tuple, list)):
		dt = [dt]

	for doctype in dt:		
		import_doc(get_json_path(doctype), submit=submit, overwrite=overwrite)
		
def get_json_path(doctype):
	return os.path.join(os.path.dirname(__file__), "demo_docs", doctype+".json")