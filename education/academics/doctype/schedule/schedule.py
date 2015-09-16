# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Schedule(Document):
	def validate(self):
		self.title = self.subject + " by " + self.employee_name
