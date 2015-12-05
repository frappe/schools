# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class candidate(Document):
	def validate(self):
		self.title = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))
		
		if self.candidate_applicant:
			self.check_unique()
			self.update_applicant_status()
		
	def check_unique(self):
		"""Validates if the candidate Applicant is Unique"""
		candidate = frappe.db.sql("select name from `tabcandidate` where candidate_applicant=%s and name!=%s", (self.candidate_applicant, self.name))
		if candidate:
			frappe.throw("candidate {0} exist against candidate applicant {1}".format(candidate[0][0], self.candidate_applicant))
		
	def update_applicant_status(self):
		"""Updates candidate Applicant status to Admitted"""
		if self.candidate_applicant:
			frappe.db.set_value("candidate Applicant", self.candidate_applicant, "application_status", "Admitted")

