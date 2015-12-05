frappe.ui.form.on("candidate", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("candidate Groups"), function() {
			frappe.route_options = {
				"candidate Group candidate.candidate": frm.doc.name
			}
			frappe.set_route("List", "candidate Group");
		});
		
		frm.add_custom_button(__("Fees"), function() {
			frappe.route_options = {
				candidate: frm.doc.name
			}
			frappe.set_route("List", "Fees");
		});
		
		frm.add_custom_button(__("Attendance"), function() {
			frappe.route_options = {
				candidate: frm.doc.name
			}
			frappe.set_route("List", "candidate Attendance");
		});	
		
		frm.add_custom_button(__("Examination"), function() {
			frappe.route_options = {
				"Examination Result.candidate": frm.doc.name
			}
			frappe.set_route("List", "Examination");
		});	
	}
});