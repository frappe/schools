# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Discussion(Document):
	def validate(self):
		if not self.owner== frappe.session.user:
			frappe.throw(_("Not Permitted"))