cur_frm.add_fetch("candidate", "title", "candidate_name");

frappe.ui.form.on("candidate Group", "refresh", function(frm) {
	if(!frm.doc.__islocal) {
		frm.add_custom_button(__("Course Schedule"), function() {
			frappe.route_options = {
				candidate_group: frm.doc.name
			}
			frappe.set_route("List", "Course Schedule");
		});
		
		frm.add_custom_button(__("Examination"), function() {
			frappe.route_options = {
				candidate_group: frm.doc.name
			}
			frappe.set_route("List", "Examination");
		});
	}
});