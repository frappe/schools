frappe.ui.form.on("Course Schedule", "refresh", function(frm) {
	if(!cur_frm.doc.__islocal) {
		frappe.call({
			method: "education.academics.doctype.student_attendance_tool.student_attendance_tool.check_attendance_records_exist",
			args: {
				"course_schedule": cur_frm.doc.name
			},
			callback: function(r) {
				if(r.message) {
					frm.add_custom_button(__("View attendance"), function() {
						frappe.route_options = {
							course_schedule: frm.doc.name
						}
						frappe.set_route("List", "Student attendance");
					});
				}
				else {
					frm.add_custom_button(__("Mark attendance"), function() {
						var att = frappe.model.make_new_doc_and_get_name('Student Attendance Tool');
						att = locals['Student Attendance Tool'][att];
						att.course_schedule = frm.doc.name;
						loaddoc('Student Attendance Tool', att.name);
					});
				}
			}
		});
	}
});