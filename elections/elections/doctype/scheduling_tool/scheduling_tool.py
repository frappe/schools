# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import calendar
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_days, getdate
from schools.utils import OverlapError

class SchedulingTool(Document):
	def schedule_course(self):
		"""Creates course schedules as per specified parametes"""
		
		course_schedules= []
		course_schedules_errors= []
		rescheduled= []
		reschedule_errors= []
		
		self.validate_mandatory()
		self.validate_date()
		
		if self.rechedule:
			rescheduled, reschedule_errors = self.delete_course_schedule(rescheduled, reschedule_errors)
		
		date = self.course_start_date
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
		if rescheduled:
			frappe.msgprint(_("Course Schedules deleted:") + "\n" + "\n".join(rescheduled))
		if reschedule_errors:
			frappe.msgprint(_("There were errors while deleting following schedules:") + "\n" + "\n".join(reschedule_errors))
			
	def validate_mandatory(self):
		"""Validates all mandatory fields"""
		fields = ['student_group', 'room', 'instructor', 'from_time', 'to_time', 'course_start_date', 'course_end_date', 'day']
		for d in  fields:
			if not self.get(d):
				frappe.throw(_("{0} is mandatory").format(self.meta.get_label(d)))	

	def validate_date(self):
		"""Validates if Course Start Date is greater than Course End Date"""
		if self.course_start_date > self.course_end_date:
			frappe.throw("Course Start Date cannot be greater than Course End Date.")

	def delete_course_schedule(self, rescheduled, reschedule_errors):
		"""Delete all course schedule within the Date range and specified filters"""
		schedules = frappe.get_list("Course Schedule", fields=["name", "schedule_date"], filters = 
			[["student_group", "=", self.student_group],
			["schedule_date", ">=", self.course_start_date], 
			["schedule_date", "<=", self.course_end_date]])
		for d in schedules:
			try:
				if self.day == calendar.day_name[getdate(d.schedule_date).weekday()]:
					frappe.delete_doc("Course Schedule", d.name)
					rescheduled.append(d.name)
			except:
				reschedule_errors.append(d.name)
		return rescheduled, reschedule_errors
			
	def make_course_schedule(self, date):
		"""Makes a new Course Schedule.
		:param date: Date on which Course Schedule will be created."""
		
		course_schedule = frappe.new_doc("Course Schedule")
		course_schedule.student_group = self.student_group
		course_schedule.course = self.course
		course_schedule.instructor = self.instructor
		course_schedule.instructor_name = self.instructor_name
		course_schedule.room = self.room
		course_schedule.schedule_date= date
		course_schedule.from_time= self.from_time
		course_schedule.to_time= self.to_time
		return course_schedule
