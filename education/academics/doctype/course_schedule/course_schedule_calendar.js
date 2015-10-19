frappe.views.calendar["Course Schedule"] = {
	field_map: {
		"start": "from_time",
		"end": "to_time",
		"id": "name",
		"title": "title",
		"allDay": "allDay"
	},
	gantt: false,
	filters: [
		{
			"fieldtype": "Link",
			"fieldname": "student_group",
			"options": "Student Group",
			"label": __("Student Group")
		},
		{
			"fieldtype": "Link",
			"fieldname": "course",
			"options": "Course",
			"label": __("Course")
		},
		{
			"fieldtype": "Link",
			"fieldname": "employee",
			"options": "Employee",
			"label": __("Employee")
		},
		{
			"fieldtype": "Link",
			"fieldname": "room",
			"options": "Room",
			"label": __("Room")
		}
	],
	get_events_method: "education.academics.doctype.course_schedule.course_schedule.get_events"
}
