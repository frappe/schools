cur_frm.add_fetch("candidate", "title", "candidate_name");
cur_frm.add_fetch("candidate", "program", "program");

frappe.ui.form.on("Fees", {
	program: function(frm) {
		frappe.call({
			method: "schools.api.get_fee_structure",
			args: {
				"program": frm.doc.program,
				"Election_term": frm.doc.Election_term
			},
			callback: function(r) {
				if(r.message) {
					frm.set_value("fee_structure" ,r.message);
				}
			}
		});
	},

	Election_term: function() {
		frappe.ui.form.trigger("Fees", "program");
	},

	fee_structure: function(frm) {
		frm.set_value("amount" ,"");
		if (frm.doc.fee_structure) {
			frappe.call({
				method: "schools.api.get_fee_amount",
				args: {
					"fee_structure": frm.doc.fee_structure
				},
				callback: function(r) {
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(frm.doc, "Fee Amount", "amount");
							row.fees_category = d.fees_category;
							row.amount = d.amount;
						});
					}
					refresh_field("amount");
				}
			});
		}
	}
});

frappe.ui.form.on("Fee Amount", {
	amount: function(frm) {
		total_amount = 0;
		for(var i=0;i<frm.doc.amount.length;i++) {
			total_amount += frm.doc.amount[i].amount;
		}
		frm.set_value("total_amount", total_amount);
	}
});
