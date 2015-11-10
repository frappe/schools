# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class StudentAttendence(Document):
	def validate(self):
		self.validate_duplication()
		
	def validate_duplication(self):
		attendence_records= frappe.db.sql("""select name from `tabStudent Attendence` where \
			student= %s and course_schedule= %s and name != %s""",
			(self.student, self.course_schedule, self.name))
		if attendence_records:
			frappe.throw(_("Attendence Record {0} exists against Student {1} for Course Schedule {2}")
				.format(attendence_records[0][0], self.student, self.course_schedule))
