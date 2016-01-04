# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class StudentGroupCreationTool(Document):
	def get_courses(self):
		program_codes = {}
		for d in frappe.get_list("Program", fields=["name", "program_code"]):
			program_codes.update({d.name: d.program_code})
			
		course_codes = {}
		for d in frappe.get_list("Course", fields=["name", "course_code"]):
			course_codes.update({d.name: d.course_code})
		
		if self.program:
			courses = frappe.db.sql("""select course, parent as program, "student_group_name" 
				from `tabProgram Course` where academic_term= %s and parent= %s""", 
				(self.academic_term, self.program), as_dict=1)
		else:
			courses = frappe.db.sql("""select course, parent as program, "student_group_name" 
				from `tabProgram Course` where academic_term= %s""", 
				self.academic_term, as_dict=1)
		
		for d in courses:
			p_code = program_codes.get(d.program)
			c_code = course_codes.get(d.course)
			
			if p_code and c_code:
				d.student_group_name = p_code + "-" + c_code + "-" + self.academic_year
			else:
				d.student_group_name = None
				
		return courses
		
	def create_student_groups(self):
		for d in self.courses:
			if not d.student_group_name:
				frappe.throw(_("""Student Group Name is mandatory"""))
			
			student_group = frappe.new_doc("Student Group")
			student_group.group_name = d.student_group_name
			student_group.course = d.course
			student_group.max_strength = d.max_strength
			student_group.academic_term = self.academic_term
			student_group.academic_year = self.academic_year
			student_group.save()
		
		frappe.msgprint(_("Student Groups created."))

