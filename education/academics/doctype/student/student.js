frappe.ui.form.on("Student", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("Fees"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Fees");
		});
		
		frm.add_custom_button(__("Student Group"), function() {
			frappe.route_options = {
				"Group Student.student": frm.doc.name
			}
			frappe.set_route("List", "Student Group");
		});	
		
		frm.add_custom_button(__("Student Attendance"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Student Attendance");
		});	
		
		frm.add_custom_button(__("Exam Result"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Exam Result");
		});	
	}
});