# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class candidateAttendance(Document):
	def validate(self):
		self.validate_duplication()
		
	def validate_duplication(self):
		"""Check if the Attendance Record is Unique"""
		attendance_records= frappe.db.sql("""select name from `tabcandidate Attendance` where \
			candidate= %s and course_schedule= %s and name != %s""",
			(self.candidate, self.course_schedule, self.name))
		if attendance_records:
			frappe.throw(_("Attendance Record {0} exists against candidate {1} for Course Schedule {2}")
				.format(attendance_records[0][0], self.candidate, self.course_schedule))
