frappe.ui.form.on("Student Applicant", {
	refresh: function(frm) {
		if(frm.doc.application_status== "Approved" && frm.doc.docstatus== 1 ) {
			frm.add_custom_button(__("Create Student"), function() {
				frm.events.create_student(frm)
			});
		}
	},
	
	create_student: function(frm) {
		frappe.model.open_mapped_doc({
			method: "schools.academics.doctype.student_applicant.student_applicant.make_student",
			frm: frm
		})
	}
});