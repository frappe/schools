# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def get_context(context):
	discussion = frappe.get_doc('Discussion', frappe.form_dict.discussion)
	portal_items = [{'reference_doctype': u'Topic', 'route': u"/topic?course=" + str(discussion.course), 'show_always': 0L, 'title': u'Topics'},
				{'reference_doctype': u'Discussion', 'route': u"/discussion?course=" + str(discussion.course), 'show_always': 0L, 'title': u'Discussions'},

	]
	context.no_cache = 0
	context.show_sidebar = True
	discussion.has_permission('read')
	context.sidebar_items = portal_items

	context.sidebar_title = discussion.course
	context.doc = discussion