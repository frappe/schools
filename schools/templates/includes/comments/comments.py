# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
from __future__ import unicode_literals

import frappe
import frappe.utils
from frappe.website.render import clear_cache

from frappe import _

@frappe.whitelist(allow_guest=True)
def add_comment(args=None):

	if not args:
		args = frappe.local.form_dict

	page_name = args.get("page_name")

	doc = frappe.get_doc(args["reference_doctype"], args["reference_name"])
	comment = doc.add_comment("Comment", args["comment"], comment_by=args["comment_by"])
	comment.flags.ignore_permissions = True
	comment.sender_full_name = args["comment_by_fullname"]
	comment.save()

	# since comments are embedded in the page, clear the web cache
	clear_cache(page_name)

	# notify commentors
	commentors = [d[0] for d in frappe.db.sql("""select sender from `tabCommunication`
		where
			communication_type = 'Comment' and comment_type = 'Comment'
			and reference_doctype=%s
			and reference_name=%s""", (comment.reference_doctype, comment.reference_name))]

	owner = frappe.db.get_value(doc.doctype, doc.name, "owner")
	recipients = list(set(commentors if owner=="Administrator" else (commentors + [owner])))

	message = _("{0} by {1}").format(frappe.utils.markdown(args.get("comment")), comment.sender_full_name)
	message += "<p><a href='{0}/{1}' style='font-size: 80%'>{2}</a></p>".format(frappe.utils.get_request_site_address(),
		page_name, _("View it in your browser"))

	from frappe.email.bulk import send

	send(recipients=recipients,
		subject = _("New comment on {0} {1}").format(doc.doctype, doc.name),
		message = message,
		reference_doctype=doc.doctype, reference_name=doc.name)

	template = frappe.get_template("templates/includes/comments/comment.html")

	return template.render({"comment": comment.as_dict()})
