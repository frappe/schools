# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"module_name": "Student",
			"color": "#c0392b",
			"icon": "octicon octicon-person",
			"label": _("Student"),
			"link": "List/Student",
			"doctype": "Student",
			"type": "list"
		},
		
		{
			"module_name": "Student Group",
			"color": "#d59919",
			"icon": "octicon octicon-organization",
			"label": _("Student Group"),
			"link": "List/Student Group",
			"doctype": "Student Group",
			"type": "list"
		},
		
		{
			"module_name": "Course Schedule",
			"color": "#d35400",
			"icon": "octicon octicon-calendar",
			"label": _("Course Schedule"),
			"link": "Calendar/Course Schedule",
			"doctype": "Course Schedule",
			"type": "list"
		},
		
		{
			"module_name": "Student Attendance",
			"color": "#3aacba",
			"icon": "octicon octicon-checklist",
			"label": _("Student Attendance"),
			"link": "List/Student Attendance",
			"doctype": "Student Attendance",
			"type": "list"
		},
		
		{
			"module_name": "Course",
			"color": "#9911a2",
			"icon": "octicon octicon-book",
			"label": _("Course"),
			"link": "List/Course",
			"doctype": "Course",
			"type": "list"
		},
		
		{
			"module_name": "Program",
			"color": "#9b59b6",
			"icon": "octicon octicon-repo",
			"label": _("Program"),
			"link": "List/Program",
			"doctype": "Program",
			"type": "list"
		},
		
		{
			"module_name": "Student Applicant",
			"color": "#83C21E",
			"icon": "octicon octicon-clippy",
			"label": _("Student Applicant"),
			"link": "List/Student Applicant",
			"doctype": "Student Applicant",
			"type": "list"
		},

		{
			"module_name": "Examination",
			"color": "#8a70be",
			"icon": "icon-file-text-alt",
			"label": _("Examination"),
			"link": "List/Examination",
			"doctype": "Examination",
			"type": "list"
		},
		
		{
			"module_name": "Fees",
			"color": "#83C21E",
			"icon": "icon-money",
			"label": _("Fees"),
			"link": "List/Fees",
			"doctype": "Fees",
			"type": "list"
		},
		
		{
			"module_name": "Instructor",
			"color": "#be907c",
			"icon": "octicon octicon-broadcast",
			"label": _("Instructor"),
			"link": "List/Instructor",
			"doctype": "Instructor",
			"type": "list"
		},
		
		{
			"module_name": "Room",
			"color": "#f22683",
			"icon": "icon-map-marker",
			"label": _("Room"),
			"link": "List/Room",
			"doctype": "Examination",
			"type": "list"
		},
		
		{
			"module_name": "Academics",
			"color": "#DE2B37",
			"icon": "octicon octicon-mortar-board",
			"type": "module",
			"label": _("Academics")
		}
	]
