# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def enroll_candidate(source_name):
	"""Creates a candidate Record and returns a Program Enrollment.

	:param source_name: candidate Applicant.
	"""
	candidate = get_mapped_doc("candidate Applicant", source_name,
		{"candidate Applicant": {
			"doctype": "candidate",
			"field_map": {
				"name": "candidate_applicant"
			}
		}})
	candidate.save()
	
	program_enrollment = frappe.new_doc("Program Enrollment")
	program_enrollment.candidate = candidate.name
	program_enrollment.candidate_name = candidate.title
	program_enrollment.program = frappe.db.get_value("candidate Applicant", source_name, "program")
	return program_enrollment

@frappe.whitelist()
def check_attendance_records_exist(course_schedule):
	"""Check if Attendance Records are made against the specified Course Schedule.

	:param course_schedule: Course Schedule.
	"""
	return frappe.get_list("candidate Attendance", filters={"course_schedule": course_schedule})

@frappe.whitelist()
def mark_attendance(candidates_present, candidates_absent, course_schedule):
	"""Creates Multiple Attendance Records.

	:param candidates_present: candidates Present JSON.
	:param candidates_absent: candidates Absent JSON.
	:param course_schedule: Course Schedule.
	"""
	present = json.loads(candidates_present)
	absent = json.loads(candidates_absent)

	for d in present:
		make_attendance_records(d["candidate"], d["candidate_name"], course_schedule, "Present")
		
	for d in absent:
		make_attendance_records(d["candidate"], d["candidate_name"], course_schedule, "Absent")

	frappe.msgprint(_("Attendance has been marked successfully."))

def make_attendance_records(candidate, candidate_name, course_schedule, status):
	"""Creates Attendance Record.

	:param candidate: candidate.
	:param candidate_name: candidate Name.
	:param course_schedule: Course Schedule.
	:param status: Status (Present/Absent)
	"""
	candidate_attendance = frappe.new_doc("candidate Attendance")
	candidate_attendance.candidate = candidate
	candidate_attendance.candidate_name = candidate_name
	candidate_attendance.course_schedule = course_schedule
	candidate_attendance.status = status
	candidate_attendance.submit()

@frappe.whitelist()
def get_candidate_group_candidates(candidate_group):
	"""Returns List of candidate, candidate_name in candidate Group.

	:param candidate_group: candidate Group.
	"""
	candidates = frappe.get_list("candidate Group candidate", fields=["candidate", "candidate_name"] , filters={"parent": candidate_group}, order_by= "idx")
	return candidates
	
@frappe.whitelist()
def get_fee_structure(program, Election_term=None):
	"""Returns Fee Structure.

	:param program: Program.
	:param Election_term: Election Term.
	"""
	fee_structure = frappe.db.get_values("Fee Structure", {"program": program,
		"Election_term": Election_term}, 'name', as_dict=True)
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

	data = frappe.db.sql("""select name, title, from_time, to_time, room, candidate_group
		from `tabCourse Schedule`
		where ( from_time between %(start)s and %(end)s or to_time between %(start)s and %(end)s )
		{conditions}""".format(conditions=conditions), {
			"start": start,
			"end": end
			}, as_dict=True, update={"allDay": 0})
	
	for d in data:
		d.title += " \n for " + d.candidate_group + " in Room "+ d.room

	return data