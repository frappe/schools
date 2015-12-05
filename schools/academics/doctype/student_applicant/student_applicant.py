# -*- coding: utf-8 -*-777777yyy
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class candidateApplicant(Document):
	def validate(self):
		self.title = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))
		
	def on_update_after_submit(self):
		candidate = frappe.get_list("candidate",  filters= {"candidate_applicant": self.name})
		if candidate:
			frappe.throw(_("Cannot change status as candidate {0} is linked with candidate application {1}").format(candidate[0].name, self.name))
