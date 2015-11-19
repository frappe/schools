# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.document import Document
from frappe.utils import now, get_datetime

class OverlapError(frappe.ValidationError): pass

class CourseSchedule(Document):
	def validate(self):
		self.instructor_name = frappe.db.get_value("Instructor", self.instructor, "instructor_name")
		self.set_title()
		self.validate_date()
		self.validate_overlap()
		
	def set_title(self):
		self.title = self.course + " by " + (self.instructor_name if self.instructor_name else self.instructor)

	def validate_date(self):
		if get_datetime(self.from_time) < get_datetime(now()):
			frappe.throw("From Time cannot be lesser than System Time.")
		elif self.from_time > self.to_time:
			frappe.throw("From Time cannot be greater than To Time.")
	
	def validate_overlap(self):
		self.validate_overlap_for("student_group")
		self.validate_overlap_for("instructor")
		self.validate_overlap_for("room")

	def validate_overlap_for(self, fieldname):
		existing = self.get_overlap_for(fieldname)
		if existing:
			frappe.throw(_("This Course Schedule conflicts with {0} for {1} {2}").format(existing.name,
				self.meta.get_label(fieldname), self.get(fieldname)), OverlapError)
		
	def get_overlap_for(self, fieldname):
		if not self.get(fieldname):
			return

		existing = frappe.db.sql("""select name, from_time, to_time from `tabCourse Schedule`
			where `{0}`=%(val)s and
			(
				(from_time > %(from_time)s and from_time < %(to_time)s) or
				(to_time > %(from_time)s and to_time < %(to_time)s) or
				(%(from_time)s > from_time and %(from_time)s < to_time) or
				(%(from_time)s = from_time and %(to_time)s = to_time))
			and name!=%(name)s""".format(fieldname),
			{
				"val": self.get(fieldname),
				"from_time": self.from_time,
				"to_time": self.to_time,
				"name": self.name or "No Name"
			}, as_dict=True)

		return existing[0] if existing else None
	
@frappe.whitelist()
def get_events(start, end, filters=None):
	from frappe.desk.calendar import get_event_conditions
	conditions = get_event_conditions("Course Schedule", filters)

	data = frappe.db.sql("""select name, title, from_time, to_time, room, student_group
		from `tabCourse Schedule`
		where ( from_time between %(start)s and %(end)s or to_time between %(start)s and %(end)s )
		{conditions}""".format(conditions=conditions), {
			"start": start,
			"end": end
			}, as_dict=True, update={"allDay": 0})
	
	for d in data:
		d.title += " \n for " + d.student_group + " in Room "+ d.room

	return data

@frappe.whitelist()
def check_attendance_records_exist(course_schedule):
	return frappe.get_list("Student Attendance", filters={"course_schedule": course_schedule})

@frappe.whitelist()
def mark_attendance(students_present, students_absent, course_schedule):
	present = json.loads(students_present)
	absent = json.loads(students_absent)

	for d in present:
		make_attendance_records(d["student"], d["student_name"], course_schedule, "Present")
		
	for d in absent:
		make_attendance_records(d["student"], d["student_name"], course_schedule, "Absent")

	frappe.msgprint(_("Attendance has been marked successfully."))
	
def make_attendance_records(student, student_name, course_schedule, status):
	student_attendance = frappe.new_doc("Student Attendance")
	student_attendance.student = student
	student_attendance.student_name = student_name
	student_attendance.course_schedule = course_schedule
	student_attendance.status = status
	student_attendance.submit()
