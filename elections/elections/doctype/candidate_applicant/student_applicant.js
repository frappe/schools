frappe.ui.form.on("Student Applicant", {
	refresh: function(frm) {
		if(frm.doc.application_status== "Approved" && frm.doc.docstatus== 1 ) {
			frm.add_custom_button(__("Enroll"), function() {
				frm.events.enroll(frm)
			}).addClass("btn-primary");
		}
	},
	
	enroll: function(frm) {
		frappe.model.open_mapped_doc({
			method: "schools.api.enroll_student",
			frm: frm
		})
	}
});