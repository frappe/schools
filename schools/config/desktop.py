# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Academics": {
			"color": "#DE2B37",
			"icon": "octicon octicon-mortar-board",
			"type": "module",
			"label": _("Academics")
		},
		
		"Student": {
			"color": "#be907c",
			"icon": "octicon octicon-person",
			"label": _("Student"),
			"link": "List/Student",
			"doctype": "Student",
			"type": "list"
		},
		
		"Student Group": {
			"color": "#d59919",
			"icon": "octicon octicon-organization",
			"label": _("Student Group"),
			"link": "List/Student Group",
			"doctype": "Student Group",
			"type": "list"
		},
		
		"Student Applicant": {
			"color": "#83C21E",
			"icon": "octicon octicon-sign-in",
			"label": _("Student Applicant"),
			"link": "List/Student Applicant",
			"doctype": "Student Applicant",
			"type": "list"
		},
		
		"Course Schedule": {
			"color": "#31E3E2",
			"icon": "octicon octicon-calendar",
			"label": _("Course Schedule"),
			"link": "Calendar/Course Schedule",
			"doctype": "Course Schedule",
			"type": "list"
		},

		"Student Attendance": {
			"color": "#3aacba",
			"icon": "octicon octicon-checklist",
			"label": _("Student Attendance"),
			"link": "List/Student Attendance",
			"doctype": "Student Attendance",
			"type": "list"
		},
		
		"Examination": {
			"color": "#8a70be",
			"icon": "octicon octicon-clippy",
			"label": _("Examination"),
			"link": "List/Examination",
			"doctype": "Examination",
			"type": "list"
		},
		
		"Fees": {
			"color": "#3b1b01",
			"icon": "icon-money",
			"label": _("Fees"),
			"link": "List/Fees",
			"doctype": "Fees",
			"type": "list"
		},
		
		"Course": {
			"color": "#9911a2",
			"icon": "octicon octicon-repo-clone",
			"label": _("Course"),
			"link": "List/Course",
			"doctype": "Course",
			"type": "list"
		},
		
		"Program": {
			"color": "#8712de",
			"icon": "octicon octicon-repo",
			"label": _("Program"),
			"link": "List/Program",
			"doctype": "Program",
			"type": "list"
		},
		
		"Instructor": {
			"color": "#E8B0C5",
			"icon": "octicon octicon-broadcast",
			"label": _("Instructor"),
			"link": "List/Instructor",
			"doctype": "Instructor",
			"type": "list"
		},
		
		"Room": {
			"color": "#f22683",
			"icon": "icon-map-marker",
			"label": _("Room"),
			"link": "List/Room",
			"doctype": "Examination",
			"type": "list"
		}

	}