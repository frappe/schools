# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class StudentApplicant(Document):
	def validate(self):
		self.title = self.first_name + " " + self.middle_name + " " +self.last_name

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
