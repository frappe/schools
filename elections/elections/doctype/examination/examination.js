cur_frm.add_fetch("candidate_group", "course", "course");
cur_frm.add_fetch("candidate", "title", "candidate_name");

frappe.ui.form.on("Examination" ,{
	candidate_group : function(frm) {
		frm.set_value("results" ,"");
		if (frm.doc.candidate_group) {
			frappe.call({
				method: "schools.elections.doctype.candidate_group.candidate_group.get_candidates",
				args: {
					"candidate_group": frm.doc.candidate_group
				},
				callback: function(r) {
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(cur_frm.doc, "Examination Result", "results");
							row.candidate = d.candidate;
							row.candidate_name = d.candidate_name;
						});
					}
					refresh_field("results");
				}
			});
		}
	}
});