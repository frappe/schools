# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class StudentAttendanceTool(Document):
	def mark_attendance(self):
		if self.students:
			att_records = []
			for d in self.students:
				student_attendance = frappe.new_doc("Student Attendance")
				student_attendance.student = d.student
				student_attendance.student_name = d.student_name
				student_attendance.course_schedule = self.course_schedule
				student_attendance.status = d.status
				student_attendance.submit()
				att_records.append(student_attendance.name)
			frappe.msgprint(_("Attendance Records created:") + "\n" + "\n".join(att_records))

@frappe.whitelist()
def get_students(student_group, course_schedule):
	if check_attendance_records_exist(course_schedule):
		frappe.throw(_("""Attendance Records exist for course schedule {0}""".format(course_schedule)))
	students = frappe.get_list("Group Student", fields=["student", "student_name"] , filters={"parent": student_group}, order_by= "idx")
	return students

@frappe.whitelist()
def check_attendance_records_exist(course_schedule):
	return frappe.get_list("Student Attendance", filters={"course_schedule": course_schedule})
