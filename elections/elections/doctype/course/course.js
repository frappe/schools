frappe.ui.form.on("Course", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("Program"), function() {
			frappe.route_options = {
				"Program Subject.course": frm.doc.name
			}
			frappe.set_route("List", "Program");
		});
		
		frm.add_custom_button(__("Student"), function() {
			frappe.route_options = {
				"Student Course.course": frm.doc.name
			}
			frappe.set_route("List", "Student");
		});
		
		frm.add_custom_button(__("Student Group"), function() {
			frappe.route_options = {
				course: frm.doc.name
			}
			frappe.set_route("List", "Student Group");
		});
		
		frm.add_custom_button(__("Course Schedule"), function() {
			frappe.route_options = {
				course: frm.doc.name
			}
			frappe.set_route("List", "Course Schedule");
		});
		
		frm.add_custom_button(__("Examination"), function() {
			frappe.route_options = {
				course: frm.doc.name
			}
			frappe.set_route("List", "Examination");
		});
	}
});