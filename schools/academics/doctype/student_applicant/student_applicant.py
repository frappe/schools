# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class StudentApplicant(Document):
	def validate(self):
		self.title = self.first_name 
		if self.middle_name:
			self.title += " " + self.middle_name
		if self.last_name:
			self.title += " " +self.last_name
		
	def on_update_after_submit(self):
		student = frappe.get_list("Student",  filters= {"student_applicant": self.name})
		if student:
			frappe.throw(_("Cannot change status as student {0} is linked with student application {1}").format(student[0].name, self.name))

@frappe.whitelist()
def make_student(source_name, target_doc=None):
	target_doc = get_mapped_doc("Student Applicant", source_name,
		{"Student Applicant": {
			"doctype": "Student",
			"field_map": {
				"name": "student_applicant"
			}
		}}, target_doc)

	return target_doc
