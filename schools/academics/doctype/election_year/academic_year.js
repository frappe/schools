frappe.ui.form.on("Election Year", "refresh", function(frm) {
	if(!frm.doc.__islocal) {
		frm.add_custom_button(__("candidate Group"), function() {
			frappe.route_options = {
				Election_year: frm.doc.name
			}
			frappe.set_route("List", "candidate Group");
		});
	}
});