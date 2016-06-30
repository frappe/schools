# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe

def get_context(context):
	announcement = frappe.get_doc('Announcement', frappe.form_dict.announcement)
	context.no_cache = 1
	context.show_sidebar = True
	announcement.has_permission('read')
	context.doc = announcement
	attachments = frappe.db.sql("""select file_url, file_name from tabFile as file
								where file.attached_to_name=%s """,(announcement.name), as_dict = True)

	for file in attachments:
		file.thumbnail_url = get_thumbail(file.file_url, announcement.name)

	context.attached_files = attachments

def get_thumbail(file_url, attached_to_name):
	if file_url:
		try:
			file_doc = frappe.get_doc("File", {
			"file_url": file_url,
			"attached_to_doctype": "Announcement",
			"attached_to_name": attached_to_name
			})
		except IOError:
			file_url = None

		except frappe.DoesNotExistError:
			pass
			frappe.local.message_log.pop()

	if file_doc:
		if not file_doc.thumbnail_url:
			return file_doc.make_thumbnail()

