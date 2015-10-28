# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import calendar
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, getdate, get_datetime
from education.academics.doctype.course_schedule.course_schedule import OverlapError

class SchedulingTool(Document):
	def schedule_course(self):
		date = self.course_start_date
		course_schedules= []
		course_schedules_errors=[]
		
		while(date < self.course_end_date):
			if self.day == calendar.day_name[getdate(date).weekday()]:
				course_schedule = self.make_course_schedule(date)
				try:
					course_schedule.save()
				except OverlapError:
					course_schedules_errors.append(date)
				else:
					course_schedules.append(course_schedule.name + " on " + date)
				
				date = add_days(date, 7)
			else:
				date = add_days(date, 1)
			
		frappe.local.message_log = []
		if course_schedules:
			frappe.msgprint(_("Course Schedules created:") + "\n" + "\n".join(course_schedules))
		if course_schedules_errors:
			frappe.msgprint(_("There were errors while scheduling course on :") + "\n" + "\n".join(course_schedules_errors))

	def make_course_schedule(self, date):
		course_schedule = frappe.new_doc("Course Schedule")
		course_schedule.student_group = self.student_group
		course_schedule.course = self.course
		course_schedule.employee = self.employee
		course_schedule.employee_name = self.employee_name
		course_schedule.room = self.room
		course_schedule.from_time=  get_datetime(date + " " + self.from_time)
		course_schedule.to_time=  get_datetime(date + " " + self.to_time)
		return course_schedule
		