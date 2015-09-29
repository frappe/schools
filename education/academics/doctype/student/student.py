# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Student(Document):
	def validate(self):
		self.title = self.first_name + " " + self.middle_name + " " +self.last_name
		self.update_applicant_status()
		
	def update_applicant_status(self):
		if self.student_applicant:
			frappe.db.set_value("Student Applicant", self.student_applicant, "status", "Student")
	