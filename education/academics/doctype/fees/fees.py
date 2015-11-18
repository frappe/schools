# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Fees(Document):
	def validate(self):
		self.calculate_total()
		
	def calculate_total(self):
		self.total_amount = 0
		for d in self.amount:
			self.total_amount += d.amount
	
@frappe.whitelist()
def get_fee_structure(program, academic_term=None):
	fee_structure = frappe.db.get_values("Fee Structure", {"program": program,
		"academic_term": academic_term}, 'name', as_dict=True)
	return fee_structure[0].name if fee_structure else None
	

@frappe.whitelist()
def get_fee_amount(fee_structure):
	fs = frappe.get_list("Fee Amount", fields=["fees_category", "amount"] , filters={"parent": fee_structure}, order_by= "idx")
	return fs
