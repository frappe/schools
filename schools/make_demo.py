# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

import frappe, os, json
from frappe.core.page.data_import_tool.data_import_tool import import_doc
from schools.simulate import simulate
from frappe.utils.make_random import get_random
from datetime import datetime
import time, random

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
	make_fees_category()
	make_fees_structure()
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
	frappe.db.commit()
	
def make_student_applicants():
	blood_group = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
	male_names = []
	female_names = []
	
	file_path = get_json_path("Random Student Data")
	with open(file_path, "r") as open_file:
		random_student_data = json.loads(open_file.read())
		count = 1
		
		for d in random_student_data:
			if d.get('gender') == "Male":
				male_names.append(d.get('first_name').title())

			if d.get('gender') == "Female":
				female_names.append(d.get('first_name').title())
			
		for idx, d in enumerate(random_student_data):
			student_applicant = frappe.new_doc("Student Applicant")
			student_applicant.first_name = d.get('first_name').title()
			student_applicant.last_name = d.get('last_name').title()
			student_applicant.student_email_id = student_applicant.first_name + student_applicant.last_name + str(idx) + "@example.com"
			student_applicant.image = d.get('image')
			student_applicant.gender = d.get('gender')
			student_applicant.program = get_random("Program")
			student_applicant.blood_group = random.choice(blood_group)
			year = random.randint(1990, 1998)
			month = random.randint(1, 12)
			day = random.randint(1, 28)
			student_applicant.date_of_birth = datetime(year, month, day)
			student_applicant.mother_name = random.choice(female_names) + " " + d.get('last_name').title()
			student_applicant.father_name = random.choice(male_names) + " " + d.get('last_name').title()
			if student_applicant.gender == "Male":
				student_applicant.middle_name = random.choice(male_names)
			else:
				student_applicant.middle_name = random.choice(female_names)

			if count <5:
				student_applicant.insert()
				frappe.db.commit()
			else:
				student_applicant.submit()
				frappe.db.commit()
			count+=1

def make_student_group():
	for d in frappe.db.get_list("Academic Term"):
		sg_tool = frappe.new_doc("Student Group Creation Tool")
		sg_tool.academic_year = "2016-17"
		sg_tool.academic_term = d.name
		sg_tool.courses = sg_tool.get_courses()
		sg_tool.create_student_groups()
		frappe.db.commit()

def make_fees_category():
	fee_type = ["Tuition Fee", "Hostel Fee", "Logistics Fee", 
				"Medical Fee", "Mess Fee", "Security Deposit"]

	fee_desc = {"Tuition Fee" : "Curricular activities which includes books, notebooks and faculty charges" , 
				"Hostel Fee" : "Stay of students in institute premises", 
				"Logistics Fee" : "Lodging boarding of the students" , 
				"Medical Fee" : "Medical welfare of the students", 
				"Mess Fee" : "Food and beverages for your ward", 
				"Security Deposit" : "In case your child is found to have damaged institutes property"
				}

	for i in fee_type:
		fee_category = frappe.new_doc("Fee Category")
		fee_category.category_name = i
		fee_category.description = fee_desc[i]
		fee_category.insert()
		frappe.db.commit()

def make_fees_structure():
	for i in xrange(1,6):
		fee_structure = frappe.new_doc("Fee Structure")
		fee_structure.name = "FS00" + str(i)
		fee_structure.program = random.choice(frappe.db.get_list("Program")).name
		fee_structure.academic_term = random.choice(frappe.db.get_list("Academic Term")).name
		for j in range(1,3):
			temp = {"fees_category": random.choice(frappe.db.get_list("Fee Category")).name , "amount" : random.randint(500,1000)}
			fee_structure.append("amount", temp)
		fee_structure.insert()
		frappe.db.commit()

def import_data(dt, submit=False, overwrite=False):
	if not isinstance(dt, (tuple, list)):
		dt = [dt]

	for doctype in dt:		
		import_doc(get_json_path(doctype), submit=submit, overwrite=overwrite)
		
def get_json_path(doctype):
	return os.path.join(os.path.dirname(__file__), "demo_docs", doctype+".json")