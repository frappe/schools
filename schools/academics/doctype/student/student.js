frappe.ui.form.on("Student", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frm.dashboard.heatmap_message = __('This is based on the attendance of this Student');
		frm.dashboard.show_heatmap = true;
		frm.dashboard.show_dashboard();
	}
});