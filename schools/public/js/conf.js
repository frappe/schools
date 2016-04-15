// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide('schools');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "Schools";

	frappe.help_feedback_link = '<p><a class="text-muted" \
		href="https://discuss.erpnext.com">Feedback</a></p>'


	$('.navbar-home').html('<img class="erpnext-icon" src="'+
			frappe.urllib.get_base_url()+'/assets/erpnext/images/erp-icon.svg" />');

	$('[data-link="docs"]').attr("href", "http://frappe.github.io/schools/")
});
