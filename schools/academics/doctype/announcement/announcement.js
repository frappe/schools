// Copyright (c) 2016, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Announcement', {
	refresh: function(frm) {
		frm.toggle_reqd("student", frm.doc.receiver=="Student")
		frm.toggle_reqd("student_group", frm.doc.receiver=="Student Group")
	}
});
