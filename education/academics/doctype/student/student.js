frappe.ui.form.on("Student", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("Fees"), function() {
			frappe.route_options = {
				student: frm.doc.name
			}
			frappe.set_route("List", "Fees");
		});
		
	}
});