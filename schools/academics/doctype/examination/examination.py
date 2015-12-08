# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
class OverlapError(frappe.ValidationError): pass

class Examination(Document):
	def validate(self):
		self.validate_overlap()
	
	def validate_overlap(self):
		"""Validates overlap for Student Group, Supervisor, Room"""
		self.validate_overlap_for("student_group")
		self.validate_overlap_for("supervisor")
		self.validate_overlap_for("room")

	def validate_overlap_for(self, fieldname):
		"""Checks overlap for specified feild.
	
		:param fieldname: Checks Overlap for this feild 
		"""
		existing = self.get_overlap_for(fieldname)
		if existing:
			frappe.throw(_("This Examination Schedule conflicts with {0} for {1} {2}").format(existing.name,
				self.meta.get_label(fieldname), self.get(fieldname)), OverlapError)
	
	def get_overlap_for(self, fieldname):
		"""Returns overlaping document for specified feild.
	
		:param fieldname: Checks Overlap for this feild 
		"""
		if not self.get(fieldname):
			return

		existing = frappe.db.sql("""select name from `tabExamination`
			where `{0}`=%(val)s and exam_date = %(exam_date)s and
			(
				(from_time > %(from_time)s and from_time < %(to_time)s) or
				(to_time > %(from_time)s and to_time < %(to_time)s) or
				(%(from_time)s > from_time and %(from_time)s < to_time) or
				(%(from_time)s = from_time and %(to_time)s = to_time))
			and name!=%(name)s""".format(fieldname),
			{
				"exam_date": self.exam_date,
				"val": self.get(fieldname),
				"from_time": self.from_time,
				"to_time": self.to_time,
				"name": self.name or "No Name"
			}, as_dict=True)

		return existing[0] if existing else None
	

