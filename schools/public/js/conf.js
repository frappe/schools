// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.provide('schools');

// add toolbar icon
$(document).bind('toolbar_setup', function() {
	frappe.app.name = "Schools";
	$('[data-link="docs"]').attr("href", "http://frappe.github.io/schools/")
	$('[data-link="issues"]').attr("href", "https://github.com/frappe/schools/issues")
});