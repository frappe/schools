# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.desk.doctype.desktop_icon.desktop_icon import set_hidden

def setup_complete(args=None):
	create_academic_term()
	create_academic_year()
	create_program(args)
	create_course(args)
	create_instructor(args)
	create_room(args)
	block_modules()
	disable_roles()
	
def create_academic_term():
	at = ["Semester 1", "Semester 2", "Semester 3"]
	for d in at:
		academic_term = frappe.new_doc("Academic Term")
		academic_term.term_name = d
		academic_term.save()

def create_academic_year():
	ac = ["2013-14", "2014-15", "2015-16", "2016-17", "2017-18"]
	for d in ac:
		academic_year = frappe.new_doc("Academic Year")
		academic_year.academic_year_name = d
		academic_year.save()

def create_program(args):
	for i in xrange(1,6):
		if args.get("program_" + str(i)):
			program = frappe.new_doc("Program")
			program.program_name = args.get("program_" + str(i))
			program.save()

def create_course(args):
	for i in xrange(1,6):
		if args.get("course_" + str(i)):
			course = frappe.new_doc("Course")
			course.course_name = args.get("course_" + str(i))
			course.save()

def create_instructor(args):
	for i in xrange(1,6):
		if args.get("instructor_" + str(i)):
			instructor = frappe.new_doc("Instructor")
			instructor.instructor_name = args.get("instructor_" + str(i))
			instructor.save()
	
def create_room(args):
	for i in xrange(1,6):
		if args.get("room_" + str(i)):
			room = frappe.new_doc("Room")
			room.room_name = args.get("room_" + str(i))
			room.seating_capacity = args.get("room_capacity_" + str(i))
			room.save()

def block_modules():
	enabled_modules= ["Stock", "Website", "HR", "Learn"]
	
	all_erpnext_modules = frappe.get_list("Desktop Icon", fields=["module_name"], filters={'app': 'erpnext'})
	for module in all_erpnext_modules:
		if module.module_name not in enabled_modules:
			set_hidden(module.module_name)

def disable_roles():
	enabled_roles_list = ["Guest", "Administrator", "System Manager", "All", "Academics User"]
	for role in frappe.get_list("Role"):
		if not role.name in enabled_roles_list:
			role_doc = frappe.get_doc("Role", role)
			role_doc.disabled = 1
			role_doc.save()
