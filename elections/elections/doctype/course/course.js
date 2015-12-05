frappe.ui.form.on("Course", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("Program"), function() {
			frappe.route_options = {
				"Program Subject.course": frm.doc.name
			}
			frappe.set_route("List", "Program");
		});
		
		frm.add_custom_button(__("candidate"), function() {
			frappe.route_options = {
				"candidate Course.course": frm.doc.name
			}
			frappe.set_route("List", "candidate");
		});
		
		frm.add_custom_button(__("candidate Group"), function() {
			frappe.route_options = {
				course: frm.doc.name
			}
			frappe.set_route("List", "candidate Group");
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