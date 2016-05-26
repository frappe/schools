# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json

def get_context(context):
	
	context.no_cache = 1
	context.show_sidebar = True
	exam = frappe.get_doc('Examination', frappe.form_dict.exam)
	
	context.doc = exam