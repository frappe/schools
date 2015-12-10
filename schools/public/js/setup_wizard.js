frappe.provide("schools.wiz");

frappe.pages['setup-wizard'].on_page_load = function(wrapper) {
	if(sys_defaults.company) {
		frappe.set_route("desk");
		return;
	}
};

function load_schools_slides() {
	$.extend(schools.wiz, {
		program: {
			"title": __("Program"),
			"help": __("Example: Masters in Computer Science"),
			"fields": [],
			before_load: function(slide) {
				slide.fields = [];
				for(var i=1; i<6; i++) {
					slide.fields = slide.fields.concat([
						{fieldtype:"Section Break", show_section_border: true},
						{fieldtype:"Data", fieldname:"program_" + i, label:__("Program") + " " + i, placeholder: __("Program Name")},
					])
				}
				slide.fields[1].reqd = 1;
			},
			css_class: "single-column"
		},
		
		course: {
			"title": __("Course"),
			"help": __("Example: Basic Mathematics"),
			"fields": [],
			before_load: function(slide) {
				slide.fields = [];
				for(var i=1; i<6; i++) {
					slide.fields = slide.fields.concat([
						{fieldtype:"Section Break", show_section_border: true},
						{fieldtype:"Data", fieldname:"course_" + i, label:__("Course") + " " + i,  placeholder: __("Course Name")},
					])
				}
				slide.fields[1].reqd = 1;
			},
			css_class: "single-column"
		},
		
		
		instructor: {
			"title": __("Instructor"),
			"help": __("People who teach at your organisation"),
			"fields": [],
			before_load: function(slide) {
				slide.fields = [];
				for(var i=1; i<6; i++) {
					slide.fields = slide.fields.concat([
						{fieldtype:"Section Break", show_section_border: true},
						{fieldtype:"Data", fieldname:"instructor_" + i, label:__("Instructor") + " " + i,  placeholder: __("Instructor Name")},
					])
				}
				slide.fields[1].reqd = 1;
			},
			css_class: "single-column"
		},
		
		room: {
			"title": __("Room"),
			"help": __("Classrooms/ Laboratories etc where lectures can be scheduled."),
			"fields": [],
			before_load: function(slide) {
				slide.fields = [];
				for(var i=1; i<4; i++) {
					slide.fields = slide.fields.concat([
						{fieldtype:"Section Break", show_section_border: true},
						{fieldtype:"Data", fieldname:"room_" + i, label:__("Room") + " " + i},
						{fieldtype:"Column Break"},
						{fieldtype:"Int", fieldname:"room_capacity_" + i, label:__("Room") + " " + i + " Capacity"},
					])
				}
				slide.fields[1].reqd = 1;
			},
			css_class: "two-column"
		},
		
	});


};

frappe.wiz.on("before_load", function() {
	load_schools_slides();
	frappe.wiz.add_slide(schools.wiz.program);
	frappe.wiz.add_slide(schools.wiz.course);
	frappe.wiz.add_slide(schools.wiz.instructor);
	frappe.wiz.add_slide(schools.wiz.room);

});

