# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import calendar
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, getdate, get_datetime

class SchedulingTool(Document):
	def schedule_course(self):
		date = self.course_start_date
		course_schedules= []
		
		while(date < self.course_end_date):
			if self.day == calendar.day_name[getdate(date).weekday()]:
				course_schedule = self.make_course_schedule(date)
				course_schedule.save()
				course_schedules.append(course_schedule.name)
				date = add_days(date, 7)
			else:
				date = add_days(date, 1)
				
		if course_schedules:
			frappe.local.message_log = []
			frappe.msgprint(_("Course Schedules created:") + "\n" + "\n".join(course_schedules))
		

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
		