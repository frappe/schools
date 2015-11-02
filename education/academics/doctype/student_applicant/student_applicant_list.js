frappe.listview_settings['Student Applicant'] = {
	add_fields: [ "application_status"],
	get_indicator: function(doc) {
		if (doc.application_status=="Applied") {
			return [__("Applied"), "orange", "status,=,Applied"];
		}
		else if (doc.application_status=="Approved") {
			return [__("Approved"), "green", "status,=,Approved"];
		}
		else if (doc.application_status=="Admitted") {
			return [__("Admitted"), "blue", "status,=,Admitted"];
		}
	}
};