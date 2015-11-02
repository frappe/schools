frappe.ui.form.on("Student Applicant", "refresh", function(frm) {
	if(frm.doc.application_status== "Approved" && frm.doc.docstatus== 1 ) {
		frm.add_custom_button(__("Create Student"), cur_frm.cscript.create_student, "btn-default");
	}
});

cur_frm.cscript.create_student = function() {
	frappe.model.open_mapped_doc({
		method: "education.academics.doctype.student_applicant.student_applicant.make_student",
		frm: cur_frm
	})
}
