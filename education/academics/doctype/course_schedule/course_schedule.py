# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CourseSchedule(Document):
	def validate(self):
		self.set_title()
		
	def set_title(self):
		self.title = self.course + " by " + self.employee_name
	
	
@frappe.whitelist()
def get_events(start, end, filters=None):
	from frappe.desk.calendar import get_event_conditions
	conditions = get_event_conditions("Course Schedule", filters)

	data = frappe.db.sql("""select name, title, from_time, to_time, room, student_group
		from `tabCourse Schedule`
		where ( from_time between %(start)s and %(end)s or to_time between %(start)s and %(end)s )
		{conditions}""".format(conditions=conditions), {
			"start": start,
			"end": end
			}, as_dict=True, update={"allDay": 0})
	
	for d in data:
		d.title += " \n for " + d.student_group + " in R	oom "+ d.room

	return data
