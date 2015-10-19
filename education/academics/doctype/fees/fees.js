cur_frm.add_fetch("student", "title", "student_name");
cur_frm.add_fetch("student", "program", "program");

frappe.ui.form.on("Fees", "program", function() {
	frappe.call({
		method: "education.academics.doctype.fees.fees.get_fee_structure",
		args: {
			"program": cur_frm.doc.program,
			"academic_term": cur_frm.doc.academic_term
		},
		callback: function(r) {
			if(r.message) {
				cur_frm.set_value("fee_structure" ,r.message);
			}
		}
	});
})

frappe.ui.form.on("Fees", "academic_term", function() {
	frappe.ui.form.trigger("Fees", "program");
})

frappe.ui.form.on("Fees", "fee_structure", function() {
	cur_frm.set_value("amount" ,"");
	if (cur_frm.doc.fee_structure) {
		frappe.call({
			method: "education.academics.doctype.fees.fees.get_fee_amount",
			args: {
				"fee_structure": cur_frm.doc.fee_structure
			},
			callback: function(r) {
				if (r.message) {
					$.each(r.message, function(i, d) {
						var row = frappe.model.add_child(cur_frm.doc, "Fee Amount", "amount");
						row.fees_category = d.fees_category;
						row.amount = d.amount;
					});
				}
				refresh_field("amount");
			}
		});
	}
})