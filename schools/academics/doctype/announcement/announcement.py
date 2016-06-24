# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Announcement(Document):
	pass

def get_message_list(doctype, txt, filters, limit_start, limit_page_length=20):
	user = frappe.session.user
	student = frappe.db.sql("select name from `tabStudent` where student_email_id= %s", user)
	if student:
		sg_list = frappe.db.sql("""select parent from `tabStudent Group Student` as sgs
				where sgs.student = %s """,(student))

		return frappe.db.sql("""select * from `tabAnnouncement` as notif
			where (notif.receiver = "Student" and notif.student = %s)
			or (notif.receiver = "Student Group" and notif.student_group in %s)
			and notif.docstatus = 1	
			order by notif.idx asc limit {0} , {1}"""
			.format(limit_start, limit_page_length), (student,sg_list), as_dict = True)

def get_list_context(context=None):
	return {
		"show_sidebar": True,
		'no_breadcrumbs': True,
		"title": _("Announcements"),
		"get_list": get_message_list,
		"row_template": "templates/includes/announcement/announcement_row.html"
	}