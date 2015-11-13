frappe.provide("education")

cur_frm.add_fetch("course_schedule", "from_time", "from_time");
cur_frm.add_fetch("course_schedule", "to_time", "to_time");
cur_frm.add_fetch("course_schedule", "student_group", "student_group");
cur_frm.add_fetch("course_schedule", "course", "course");
cur_frm.add_fetch("course_schedule", "instructor_name", "instructor_name");

frappe.ui.form.on("Student Attendance Tool", {
	
	on_load: function(frm){
		if (frm.doc.course_schedule) {
			frappe.ui.form.trigger("Student Attendance Tool", "course_schedule");
		}
	},
	
	refresh: function(frm) {
		frm.disable_save();
		frm.page.set_primary_action(__("Mark attendance"), function() {
			if (frm.doc.course_schedule) {
				frappe.call({
					method: "mark_attendance",
					doc:frm.doc
				})
			}
		});
	},
	
	course_schedule: function(frm) {
		frm.set_value("students" ,"");
		if (frm.doc.student_group) {
			frappe.call({
				method: "education.academics.doctype.student_attendance_tool.student_attendance_tool.get_students",
				args: {
					"student_group": cur_frm.doc.student_group,
					"course_schedule": cur_frm.doc.course_schedule
				},
				callback: function(r) {
					if (r.message) {
						$.each(r.message, function(i, d) {
							var row = frappe.model.add_child(cur_frm.doc, "Attendance Tool Student", "students");
							row.student = d.student;
							row.student_name = d.student_name;
						});
					}
					refresh_field("students");
					frm.events.get_students(frm)
				}
			});
		}
		
	},
	
	get_students: function(frm) {
		if(!frm.students_area) {
		frm.students_area = $('<div>')
			.appendTo(frm.fields_dict.students_html.wrapper);
		}
		frm.students_editor = new education.StudentsEditor(frm, frm.students_area)
	}
});

education.StudentsEditor = Class.extend({
	init: function(frm, wrapper) {
		this.wrapper = wrapper;
		this.frm = frm;
		this.make(frm);
		this.bind(frm);
	},
	make: function(frm) {
		var me = this;
		
		$(this.wrapper).empty();
		var role_toolbar = $('<p>\
			<button class="btn btn-default btn-add btn-sm" style="margin-right: 5px;"></button>\
			<button class="btn btn-sm btn-default btn-remove"></button></p>').appendTo($(this.wrapper));

		role_toolbar.find(".btn-add")
			.html(__('Check all'))
			.on("click", function() {
			$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
				if(!$(check).is(":checked")) {
					check.checked = true;
					$(check).trigger('change');
				}
			});
		});

		role_toolbar.find(".btn-remove")
			.html(__('Uncheck all'))
			.on("click", function() {
			$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
				if($(check).is(":checked")) {
					check.checked = false;
					$(check).trigger('change');
				}
			});
		});
		
		$.each(this.frm.doc.students, function(i, m) {
			$(repl('<div class="col-sm-6">\
				<div class="checkbox">\
				<label><input type="checkbox" class="students-check" student="%(student)s">\
				%(student)s</label>\
			</div></div>', {student: m.student_name})).appendTo(me.wrapper);
		});
	},
	refresh: function() {
		var me = this;
		this.wrapper.find(".students-check").prop("checked", true);
		$.each(this.frm.doc.students, function(i, d) {
			me.wrapper.find(".students-check[data-module='"+ d.student_name +"']").prop("checked", false);
		});
	},
	bind: function(frm) {
		this.wrapper.on("change", ".students-check", function() {
			var student = $(this).attr('student');
			if($(this).prop("checked")) {
				$.each(frm.doc.students, function(i, d) {
					if (d.student_name == student) {
						d.status = "Present"
					}
				});
			} else {
				$.each(frm.doc.students, function(i, d) {
					if (d.student_name == student) {
						d.status = "Absent"
					}
				});
			}
		});
	}
})