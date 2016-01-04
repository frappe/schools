# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

import sys
import frappe
import random
from frappe.utils.make_random import get_random
from schools.api import enroll_student

def simulate():
	start_date = frappe.utils.add_days(frappe.utils.nowdate(), -30)
	current_date = frappe.utils.getdate(start_date)
	runs_for = frappe.utils.date_diff(frappe.utils.nowdate(), current_date)

	for i in xrange(runs_for):
		sys.stdout.write("\rSimulating {0}".format(current_date.strftime("%Y-%m-%d")))
		sys.stdout.flush()
		frappe.local.current_date = current_date

		approve_random_student_applicant()
		enroll_random_student(current_date)

		current_date = frappe.utils.add_days(current_date, 1)

def approve_random_student_applicant():
	random_student = get_random("Student Applicant", {"application_status": "Applied"})
	if random_student:
		student_application = frappe.get_doc("Student Applicant", random_student)
		status = ["Approved", "Rejected"]
		student_application.application_status = random.choice(status)
		student_application.save()

def enroll_random_student(current_date):
	random_student = get_random("Student Applicant", {"application_status": "Approved"})
	if random_student:
		enrollment = enroll_student(random_student)
		enrollment.academic_year = get_random("Academic Year")
		enrollment.date = current_date
		enrollment.save()
		
		assign_student_group(random_student, enrollment.program)

def assign_student_group(student, program):
	prog = frappe.get_doc("Program", program)
	for d in prog.courses:
		student_group = get_random("Student Group", {"course": d})