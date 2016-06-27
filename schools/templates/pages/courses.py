# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json

def get_context(context):
		
	context.no_cache = 1
	context.show_sidebar = True
	course = frappe.get_doc('Course', frappe.form_dict.course)

	course.has_permission('read')
	
	context.doc = course

	
	context.discuss = frappe.db.sql('''select * from tabDiscussion as discuss 
							where discuss.course = %s
						''',(course.name), as_dict = True)