# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class ProgramEnrollment(Document):
	def validate(self):
		self.validate_duplication()
	
	def on_submit(self):
		self.update_student_joining_date()
	
	def validate_duplication(self):
		enrollment = frappe.db.sql("""select name from `tabProgram Enrollment` where student= %s and program= %s 
			and academic_year= %s and name != %s""", (self.student, self.program, self.academic_year, self.name))
		if enrollment:
			frappe.throw(_("Student is already enrolled."))
	
	def update_student_joining_date(self):
		date = frappe.db.sql("select min(enrollment_date) from `tabProgram Enrollment` where student= %s", self.student)
		frappe.db.set_value("Student", self.student, "joining_date", date)