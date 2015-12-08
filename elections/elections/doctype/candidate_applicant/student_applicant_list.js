frappe.listview_settings['Student Applicant'] = {
	add_fields: [ "application_status"],
	get_indicator: function(doc) {
		if (doc.application_status=="Applied") {
			return [__("Applied"), "orange", "application_status,=,Applied"];
		}
		else if (doc.application_status=="Approved") {
			return [__("Approved"), "green", "application_status,=,Approved"];
		}
		else if (doc.application_status=="Admitted") {
			return [__("Admitted"), "blue", "application_status,=,Admitted"];
		}
	}
};