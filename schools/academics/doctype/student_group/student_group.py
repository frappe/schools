# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StudentGroup(Document):
	pass

@frappe.whitelist()
def get_students(student_group):
	students = frappe.get_list("Student Group Student", fields=["student", "student_name"] , filters={"parent": student_group}, order_by= "idx")
	return students
