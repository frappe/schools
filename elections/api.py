# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.utils import cstr
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def enroll_student(source_name):
	"""Creates a Student Record and returns a Program Enrollment.

	:param source_name: Student Applicant.
	"""
	student = get_mapped_doc("Student Applicant", source_name,
		{"Student Applicant": {
			"doctype": "Student",
			"field_map": {
				"name": "student_applicant"
			}
		}})
	student.save()
	
	program_enrollment = frappe.new_doc("Program Enrollment")
	program_enrollment.student = student.name
	program_enrollment.student_name = student.title
	program_enrollment.program = frappe.db.get_value("Student Applicant", source_name, "program")
	return program_enrollment

@frappe.whitelist()
def check_attendance_records_exist(course_schedule):
	"""Check if Attendance Records are made against the specified Course Schedule.

	:param course_schedule: Course Schedule.
	"""
	return frappe.get_list("Student Attendance", filters={"course_schedule": course_schedule})

@frappe.whitelist()
def mark_attendance(students_present, students_absent, course_schedule):
	"""Creates Multiple Attendance Records.

	:param students_present: Students Present JSON.
	:param students_absent: Students Absent JSON.
	:param course_schedule: Course Schedule.
	"""
	present = json.loads(students_present)
	absent = json.loads(students_absent)

	for d in present:
		make_attendance_records(d["student"], d["student_name"], course_schedule, "Present")
		
	for d in absent:
		make_attendance_records(d["student"], d["student_name"], course_schedule, "Absent")

	frappe.msgprint(_("Attendance has been marked successfully."))

def make_attendance_records(student, student_name, course_schedule, status):
	"""Creates Attendance Record.

	:param student: Student.
	:param student_name: Student Name.
	:param course_schedule: Course Schedule.
	:param status: Status (Present/Absent)
	"""
	student_attendance = frappe.new_doc("Student Attendance")
	student_attendance.student = student
	student_attendance.student_name = student_name
	student_attendance.course_schedule = course_schedule
	student_attendance.status = status
	student_attendance.submit()

@frappe.whitelist()
def get_student_group_students(student_group):
	"""Returns List of student, student_name in Student Group.

	:param student_group: Student Group.
	"""
	students = frappe.get_list("Student Group Student", fields=["student", "student_name"] , filters={"parent": student_group}, order_by= "idx")
	return students
	
@frappe.whitelist()
def get_fee_structure(program, academic_term=None):
	"""Returns Fee Structure.

	:param program: Program.
	:param academic_term: Academic Term.
	"""
	fee_structure = frappe.db.get_values("Fee Structure", {"program": program,
		"academic_term": academic_term}, 'name', as_dict=True)
	return fee_structure[0].name if fee_structure else None
	

@frappe.whitelist()
def get_fee_amount(fee_structure):
	"""Returns Fee Amount.

	:param fee_structure: Fee Structure.
	"""
	fs = frappe.get_list("Fee Amount", fields=["fees_category", "amount"] , filters={"parent": fee_structure}, order_by= "idx")
	return fs

@frappe.whitelist()
def get_course_schedule_events(start, end, filters=None):
	"""Returns events for Course Schedule Calendar view rendering.

	:param start: Start date-time.
	:param end: End date-time.
	:param filters: Filters (JSON).
	"""
	from frappe.desk.calendar import get_event_conditions
	conditions = get_event_conditions("Course Schedule", filters)

	data = frappe.db.sql("""select name, title, schedule_date, from_time, to_time, room, student_group
		from `tabCourse Schedule`
		where ( schedule_date between %(start)s and %(end)s )
		{conditions}""".format(conditions=conditions), {
			"start": start,
			"end": end
			}, as_dict=True, update={"allDay": 0})
	
	
	for d in data:
		print d.schedule_date
		d.title += " \n for " + d.student_group + " in Room "+ d.room
		d.from_time = cstr(d.schedule_date) + " " + cstr(d.from_time)
		d.to_time = cstr(d.schedule_date) + " " + cstr(d.to_time)

	return data