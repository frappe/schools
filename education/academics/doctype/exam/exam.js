cur_frm.add_fetch("student_group", "course", "course");

frappe.ui.form.on("Exam", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.add_custom_button(__("Exam Result"), function() {
			frappe.route_options = {
				exam: frm.doc.name
			}
			frappe.set_route("List", "Exam Result");
		});
	}
});