# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe.model.document import Document

class Examination(Document):
	def validate(self):
		self.validate_overlap()
	
	def validate_overlap(self):
		"""Validates overlap for Student Group, Supervisor, Room"""

		from schools.utils import validate_overlap_for

		validate_overlap_for(self, "Examination", "student_group")
		validate_overlap_for(self, "Course Schedule", "student_group" )
		
		if self.room:
			validate_overlap_for(self, "Examination", "room")
			validate_overlap_for(self, "Course Schedule", "room")

		if self.supervisor:
			validate_overlap_for(self, "Examination", "supervisor")
			validate_overlap_for(self, "Course Schedule", "instructor", self.supervisor)