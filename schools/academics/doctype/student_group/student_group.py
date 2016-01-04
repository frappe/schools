# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class StudentGroup(Document):
	def validate(self):
		self.validate_strength()
		
	def validate_strength(self):
		if self.max_strength and len(self.students) > self.max_strength:
			frappe.throw(_("""Cannot enroll more than {0} students for this student group.""").format(self.max_strength))

