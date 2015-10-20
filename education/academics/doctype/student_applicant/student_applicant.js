cur_frm.cscript.refresh = function() {
	if(this.frm.doc.application_status== "Approved" && this.frm.doc.docstatus== 1 ) {
		this.frm.add_custom_button(__("Create Student"), cur_frm.cscript.create_student, "btn-default");
	}
}

cur_frm.cscript.create_student = function() {
	frappe.model.open_mapped_doc({
		method: "education.academics.doctype.student_applicant.student_applicant.make_student",
		frm: cur_frm
	})
}
