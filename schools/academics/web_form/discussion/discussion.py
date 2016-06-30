from __future__ import unicode_literals

import frappe

def get_context(context):
	course = frappe.get_doc('Course', frappe.form_dict.course)
	portal_items = [{'reference_doctype': u'Topic', 'route': u"/topic?course=" + str(course.name), 'show_always': 0L, 'title': u'Topics'},
				{'reference_doctype': u'Discussion', 'route': u"/discussion?course=" + str(course.name), 'show_always': 0L, 'title': u'Discussions'},

	]
	context.sidebar_items = portal_items
	context.sidebar_title = course.name

def has_website_permission(doc, ptype, user, verbose=False):
	return True