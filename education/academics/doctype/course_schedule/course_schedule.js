frappe.provide("education")

frappe.ui.form.on("Course Schedule" ,{
	refresh :function(frm) {
		if(!frm.doc.__islocal) {
			frappe.call({
				method: "education.academics.doctype.course_schedule.course_schedule.check_attendance_records_exist",
				args: {
					"course_schedule": frm.doc.name
				},
				callback: function(r) {
					if(r.message) {
						frm.events.view_attendance(frm)
					}
					else {
						frappe.call({
							method: "education.academics.doctype.student_group.student_group.get_students",
							args: {
								"student_group": frm.doc.student_group
							},
							callback: function(r) {
								if (r.message) {
									frm.events.get_students(frm, r.message)
								}
							}
						});
					}
				}
			});
		}
	},
	
	view_attendance: function(frm) {
		hide_field('attendance');
		frm.add_custom_button(__("View attendance"), function() {
			frappe.route_options = {
				course_schedule: frm.doc.name
			}
			frappe.set_route("List", "Student Attendance");
		});
	},
	
	get_students: function(frm, students) {
		if(!frm.students_area) {
		frm.students_area = $('<div>')
			.appendTo(frm.fields_dict.students_html.wrapper);
		}
		frm.students_editor = new education.StudentsEditor(frm, frm.students_area, students)
	}
});


education.StudentsEditor = Class.extend({
	init: function(frm, wrapper, students) {
		this.wrapper = wrapper;
		this.frm = frm;
		this.make(frm, students);
	},
	make: function(frm, students) {
		var me = this;
		
		$(this.wrapper).empty();
		var student_toolbar = $('<p>\
			<button class="btn btn-default btn-add btn-xs" style="margin-right: 5px;"></button>\
			<button class="btn btn-xs btn-default btn-remove" style="margin-right: 5px;"></button>\
			<button class="btn btn-default btn-primary btn-mark-att btn-xs"></button></p>').appendTo($(this.wrapper));

		student_toolbar.find(".btn-add")
			.html(__('Check all'))
			.on("click", function() {
			$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
				if(!$(check).is(":checked")) {
					check.checked = true;
				}
			});
		});

		student_toolbar.find(".btn-remove")
			.html(__('Uncheck all'))
			.on("click", function() {
			$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
				if($(check).is(":checked")) {
					check.checked = false;
				}
			});
		});
		
		student_toolbar.find(".btn-mark-att")
			.html(__('Mark Attendence'))
			.on("click", function() {
				var students_present = [];
				var students_absent = [];
				$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
					if($(check).is(":checked")) {
						students_present.push(students[i]);
					}
					else {
						students_absent.push(students[i]);
					}
				});
				frappe.call({
					method: "education.academics.doctype.course_schedule.course_schedule.mark_attendance",
					args: {
						"students_present": students_present,
						"students_absent": students_absent,
						"course_schedule": frm.doc.name
					},
					callback: function(r) {
						frm.events.view_attendance(frm)
					}
				});
		});

		
		$.each(students, function(i, m) {
			$(repl('<div class="col-sm-6">\
				<div class="checkbox">\
				<label><input type="checkbox" class="students-check" student="%(student)s">\
				%(student)s</label>\
			</div></div>', {student: m.student_name})).appendTo(me.wrapper);
		});
	}
})