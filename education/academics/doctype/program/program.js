// Copyright (c) 2015, Frappe Technologies and contributors
// For license information, please see license.txt

cur_frm.add_fetch("course", "course_code", "course_code");

frappe.ui.form.on("Program", "refresh", function(frm) {
	if(!frm.doc.__islocal) {
		frm.add_custom_button(__("Student Applicant"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "Student Applicant");
		});
		
		frm.add_custom_button(__("Student"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "Student");
		});
		
		frm.add_custom_button(__("Student Group"), function() {
			frappe.route_options = {
				program: frm.doc.name
			}
			frappe.set_route("List", "Student Group");
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