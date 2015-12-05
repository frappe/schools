# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"elections": {
			"color": "grey",
			"icon": "octicon octicon-mortar-board",
			"type": "module",
			"label": _("elections")
		}
	}
