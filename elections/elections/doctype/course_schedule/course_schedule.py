# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import now, get_datetime

class OverlapError(frappe.ValidationError): pass

class CourseSchedule(Document):
	def validate(self):
		self.instructor_name = frappe.db.get_value("Instructor", self.instructor, "instructor_name")
		self.set_title()
		self.validate_date()
		self.validate_overlap()
		
	def set_title(self):
		"""Set document Title"""
		self.title = self.course + " by " + (self.instructor_name if self.instructor_name else self.instructor)

	def validate_date(self):
		"""Validates if from_time is lesser than system time and from_time is greater than to_time"""
		if get_datetime(self.from_time) < get_datetime(now()):
			frappe.throw("From Time cannot be lesser than System Time.")
		elif self.from_time > self.to_time:
			frappe.throw("From Time cannot be greater than To Time.")
	
	def validate_overlap(self):
		"""Validates overlap for candidate Group, Instructor, Room"""
		self.validate_overlap_for("candidate_group")
		self.validate_overlap_for("instructor")
		self.validate_overlap_for("room")

	def validate_overlap_for(self, fieldname):
		"""Checks overlap for specified feild.
		
		:param fieldname: Checks Overlap for this feild 
		"""
		existing = self.get_overlap_for(fieldname)
		if existing:
			frappe.throw(_("This Course Schedule conflicts with {0} for {1} {2}").format(existing.name,
				self.meta.get_label(fieldname), self.get(fieldname)), OverlapError)
		
	def get_overlap_for(self, fieldname):
		"""Returns overlaping document for specified feild.
		
		:param fieldname: Checks Overlap for this feild 
		"""
		if not self.get(fieldname):
			return

		existing = frappe.db.sql("""select name, from_time, to_time from `tabCourse Schedule`
			where `{0}`=%(val)s and
			(
				(from_time > %(from_time)s and from_time < %(to_time)s) or
				(to_time > %(from_time)s and to_time < %(to_time)s) or
				(%(from_time)s > from_time and %(from_time)s < to_time) or
				(%(from_time)s = from_time and %(to_time)s = to_time))
			and name!=%(name)s""".format(fieldname),
			{
				"val": self.get(fieldname),
				"from_time": self.from_time,
				"to_time": self.to_time,
				"name": self.name or "No Name"
			}, as_dict=True)

		return existing[0] if existing else None
