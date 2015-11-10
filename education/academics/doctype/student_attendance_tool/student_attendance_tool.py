# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class StudentAttendanceTool(Document):
	def mark_attendence(self):
		if self.students:
			att_records = []
			for d in self.students:
				student_attendence = frappe.new_doc("Student Attendence")
				student_attendence.student = d.student
				student_attendence.student_name = d.student_name
				student_attendence.course_schedule = self.course_schedule
				student_attendence.status = d.status
				student_attendence.submit()
				att_records.append(student_attendence.name)
			frappe.msgprint(_("Attendence Records created:") + "\n" + "\n".join(att_records))

@frappe.whitelist()
def get_students(student_group, course_schedule):
	if frappe.get_list("Student Attendence", filters={"course_schedule": course_schedule}):
		frappe.throw(_("""Attendence Records exist for course schedule {0}""".format(course_schedule)))
	students = frappe.get_list("Group Student", fields=["student", "student_name"] , filters={"parent": student_group}, order_by= "idx")
	return students