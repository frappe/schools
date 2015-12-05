frappe.provide("schools")

frappe.ui.form.on("Course Schedule" ,{
	refresh :function(frm) {
		if(!frm.doc.__islocal) {
			frappe.call({
				method: "schools.api.check_attendance_records_exist",
				args: {
					"course_schedule": frm.doc.name
				},
				callback: function(r) {
					if(r.message) {
						frm.events.view_attendance(frm)
					}
					else {
						frappe.call({
							method: "schools.api.get_candidate_group_candidates",
							args: {
								"candidate_group": frm.doc.candidate_group
							},
							callback: function(r) {
								if (r.message) {
									frm.events.get_candidates(frm, r.message)
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
			frappe.set_route("List", "candidate Attendance");
		});
	},
	
	get_candidates: function(frm, candidates) {
		if(!frm.candidates_area) {
		frm.candidates_area = $('<div>')
			.appendTo(frm.fields_dict.candidates_html.wrapper);
		}
		frm.candidates_editor = new schools.candidatesEditor(frm, frm.candidates_area, candidates)
	}
});


schools.candidatesEditor = Class.extend({
	init: function(frm, wrapper, candidates) {
		this.wrapper = wrapper;
		this.frm = frm;
		this.make(frm, candidates);
	},
	make: function(frm, candidates) {
		var me = this;
		
		$(this.wrapper).empty();
		var candidate_toolbar = $('<p>\
			<button class="btn btn-default btn-add btn-xs" style="margin-right: 5px;"></button>\
			<button class="btn btn-xs btn-default btn-remove" style="margin-right: 5px;"></button>\
			<button class="btn btn-default btn-primary btn-mark-att btn-xs"></button></p>').appendTo($(this.wrapper));

		candidate_toolbar.find(".btn-add")
			.html(__('Check all'))
			.on("click", function() {
			$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
				if(!$(check).is(":checked")) {
					check.checked = true;
				}
			});
		});

		candidate_toolbar.find(".btn-remove")
			.html(__('Uncheck all'))
			.on("click", function() {
			$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
				if($(check).is(":checked")) {
					check.checked = false;
				}
			});
		});
		
		candidate_toolbar.find(".btn-mark-att")
			.html(__('Mark Attendence'))
			.on("click", function() {
				var candidates_present = [];
				var candidates_absent = [];
				$(me.wrapper).find('input[type="checkbox"]').each(function(i, check) {
					if($(check).is(":checked")) {
						candidates_present.push(candidates[i]);
					}
					else {
						candidates_absent.push(candidates[i]);
					}
				});
				frappe.call({
					method: "schools.api.mark_attendance",
					args: {
						"candidates_present": candidates_present,
						"candidates_absent": candidates_absent,
						"course_schedule": frm.doc.name
					},
					callback: function(r) {
						frm.events.view_attendance(frm)
					}
				});
		});

		
		$.each(candidates, function(i, m) {
			$(repl('<div class="col-sm-6">\
				<div class="checkbox">\
				<label><input type="checkbox" class="candidates-check" candidate="%(candidate)s">\
				%(candidate)s</label>\
			</div></div>', {candidate: m.candidate_name})).appendTo(me.wrapper);
		});
	}
})