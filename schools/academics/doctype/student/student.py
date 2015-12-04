# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Student(Document):
	def validate(self):
		self.title = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))
		
		if self.student_applicant:
			self.check_unique()
			self.update_applicant_status()
		
	def check_unique(self):
		"""Validates if the Student Applicant is Unique"""
		student = frappe.db.sql("select name from `tabStudent` where student_applicant=%s and name!=%s", (self.student_applicant, self.name))
		if student:
			frappe.throw("Student {0} exist against student applicant {1}".format(student[0][0], self.student_applicant))
		
	def update_applicant_status(self):
		"""Updates Student Applicant status to Admitted"""
		if self.student_applicant:
			frappe.db.set_value("Student Applicant", self.student_applicant, "application_status", "Admitted")

