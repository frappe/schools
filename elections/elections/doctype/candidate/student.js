frappe.ui.form.on("Student", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("Programs Enrolled"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Program Enrollment");
		});
		
		frm.add_custom_button(__("Student Groups"), function() {
			frappe.route_options = {
				"Student Group Student.student": frm.doc.name
			}
			frappe.set_route("List", "Student Group");
		});
		
		frm.add_custom_button(__("Fees"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Fees");
		});
		
		frm.add_custom_button(__("Attendance"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Student Attendance");
		});	
		
		frm.add_custom_button(__("Examination"), function() {
			frappe.route_options = {
				"Examination Result.student": frm.doc.name
			}
			frappe.set_route("List", "Examination");
		});	
	}
});