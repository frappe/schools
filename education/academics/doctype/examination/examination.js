cur_frm.add_fetch("student", "title", "student_name");

frappe.ui.form.on("Examination" ,{
	student_group : function(frm) {
		frm.set_value("results" ,"");
		if (frm.doc.student_group) {
			frappe.call({
				method: "education.academics.doctype.student_group.student_group.get_students",
				args: {
					"student_group": frm.doc.student_group
				},
				callback: function(r) {
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(cur_frm.doc, "Examination Result", "results");
							row.student = d.student;
							row.student_name = d.student_name;
						});
					}
					refresh_field("results");
				}
			});
		}
	}
});