cur_frm.cscript.refresh = function() {
	if(!this.frm.doc.__is_local == 1 ) {
		this.frm.add_custom_button(__("Collect Fees"), cur_frm.cscript.collect_fees, "btn-default");
	}
}

cur_frm.cscript.collect_fees = function() {
	frappe.prompt({fieldtype:"Link", label: __("Academic Term"), fieldname:"academic_term", options: "Academic Term"},
	function(data) {
		frappe.call({
			method: "education.academics.doctype.student.student.collect_fees",
			args: {
				"student": cur_frm.doc.name,
				"student_name": cur_frm.doc.title,
				"program": cur_frm.doc.program,
				"academic_term": data.academic_term
			},
			callback: function(r) {
				var doclist = frappe.model.sync(r.message);
				frappe.set_route("Form", doclist[0].doctype, doclist[0].name);
			}
		});
	}, __("Collect Fees"), __("Collect"));
}
