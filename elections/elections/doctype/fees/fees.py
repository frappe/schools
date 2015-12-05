# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

class Fees(Document):
	def validate(self):
		self.calculate_total()
		
	def calculate_total(self):
		"""Calculates total amount."""
		self.total_amount = 0
		for d in self.amount:
			self.total_amount += d.amount
