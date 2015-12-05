cur_frm.add_fetch("candidate_group", "program", "program");
cur_frm.add_fetch("candidate_group", "Election_year", "Election_year");
cur_frm.add_fetch("candidate_group", "Election_term", "Election_term");

frappe.ui.form.on("Scheduling Tool", "refresh", function(frm) {
	frm.disable_save();
	frm.page.set_primary_action(__("Schedule Course"), function() {
		frappe.call({
			method: "schedule_course",
			doc:frm.doc
		})
	});
});