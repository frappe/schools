// Copyright (c) 2015, Frappe Technologies and contributors
// For license information, please see license.txt

cur_frm.add_fetch("course", "course_code", "course_code");

frappe.ui.form.on("Program", "refresh", function(frm) {
	if(!frm.doc.__islocal) {
		frm.add_custom_button(__("candidate Applicant"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "candidate Applicant");
		});
		
		frm.add_custom_button(__("candidate"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "candidate");
		});
		
		frm.add_custom_button(__("candidate Group"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "candidate Group");
		});
		
		frm.add_custom_button(__("Fee Structure"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "Fee Structure");
		});
		
		frm.add_custom_button(__("Fees"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "Fees");
		});
	}
});