frappe.provide("schools.wiz");

frappe.pages['setup-wizard'].on_page_load = function(wrapper) {
	if(sys_defaults.company) {
		frappe.set_route("desk");
		return;
	}
};

function load_schools_slides() {
	$.extend(schools.wiz, {
		org: {
			app_name: "schools",
			title: __("The Organization"),
			icon: "icon-building",
			fields: [
				{fieldname:'company_name', label: __('Organization Name'), fieldtype:'Data', reqd:1,
					placeholder: __('e.g. "Hogwarts University"')},
				{fieldname:'company_abbr', label: __('Oraganization Abbreviation'), fieldtype:'Data',
					description: __('Max 5 characters'), placeholder: __('e.g. "HW"'), reqd:1},
				{fieldname:'company_tagline', label: __('What kind of an organization is it?'), fieldtype:'Data',
					placeholder:__('e.g. "High School"'), reqd:1},
				{fieldname:'bank_account', label: __('Bank Account'), fieldtype:'Data',
					placeholder: __('e.g. "XYZ National Bank"'), reqd:1 },
				{fieldname:'chart_of_accounts', label: __('Chart of Accounts'),
					options: "", fieldtype: 'Select'},

				// TODO remove this
				{fieldtype: "Section Break"},
				{fieldname:'fy_start_date', label:__('Financial Year Start Date'), fieldtype:'Date',
					description: __('Your financial year begins on'), reqd:1},
				{fieldname:'fy_end_date', label:__('Financial Year End Date'), fieldtype:'Date',
					description: __('Your financial year ends on'), reqd:1},
			],
			help: __('The name of your company for which you are setting up this system.'),

			onload: function(slide) {
				erpnext.wiz.org.load_chart_of_accounts(slide);
				erpnext.wiz.org.bind_events(slide);
				erpnext.wiz.org.set_fy_dates(slide);
			},

			validate: function() {
				// validate fiscal year start and end dates
				if (this.values.fy_start_date=='Invalid date' || this.values.fy_end_date=='Invalid date') {
					msgprint(__("Please enter valid Financial Year Start and End Dates"));
					return false;
				}

				if ((this.values.company_name || "").toLowerCase() == "company") {
					msgprint(__("Company Name cannot be Company"));
					return false;
				}

				return true;
			},

			css_class: "single-column",

			set_fy_dates: function(slide) {
				var country = slide.wiz.get_values().country;

				if(country) {
					var fy = erpnext.wiz.fiscal_years[country];
					var current_year = moment(new Date()).year();
					var next_year = current_year + 1;
					if(!fy) {
						fy = ["01-01", "12-31"];
						next_year = current_year;
					}

					slide.get_field("fy_start_date").set_input(current_year + "-" + fy[0]);
					slide.get_field("fy_end_date").set_input(next_year + "-" + fy[1]);
				}

			},

			load_chart_of_accounts: function(slide) {
				var country = slide.wiz.get_values().country;

				if(country) {
					frappe.call({
						method: "erpnext.accounts.doctype.account.chart_of_accounts.chart_of_accounts.get_charts_for_country",
						args: {"country": country},
						callback: function(r) {
							if(r.message) {
								slide.get_input("chart_of_accounts").empty()
									.add_options(r.message);

								if (r.message.length===1) {
									var field = slide.get_field("chart_of_accounts");
									field.set_value(r.message[0]);
									field.df.hidden = 1;
									field.refresh();
								}
							}
						}
					})
				}
			},

			bind_events: function(slide) {
				slide.get_input("company_name").on("change", function() {
					var parts = slide.get_input("company_name").val().split(" ");
					var abbr = $.map(parts, function(p) { return p ? p.substr(0,1) : null }).join("");
					slide.get_field("company_abbr").set_input(abbr.slice(0, 5).toUpperCase());
				}).val(frappe.boot.sysdefaults.company_name || "").trigger("change");

				slide.get_input("company_abbr").on("change", function() {
					if(slide.get_input("company_abbr").val().length > 5) {
						msgprint("Company Abbreviation cannot have more than 5 characters");
						slide.get_field("company_abbr").set_input("");
					}
				});

				// TODO remove this
				slide.get_input("fy_start_date").on("change", function() {
					var year_end_date =
						frappe.datetime.add_days(frappe.datetime.add_months(
							frappe.datetime.user_to_obj(slide.get_input("fy_start_date").val()), 12), -1);
					slide.get_input("fy_end_date").val(frappe.datetime.obj_to_user(year_end_date));

				});
			}
		},
		
		program: {
			app_name: "schools",
			title: __("Program"),
			help: __("Example: Masters in Computer Science"),
			fields: [],
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
			app_name: "schools",
			title: __("Course"),
			help: __("Example: Basic Mathematics"),
			fields: [],
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
			app_name: "schools",
			title: __("Instructor"),
			help: __("People who teach at your organisation"),
			fields: [],
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
			app_name: "schools",
			title: __("Room"),
			help: __("Classrooms/ Laboratories etc where lectures can be scheduled."),
			fields: [],
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
	frappe.wiz.remove_app_slides.push("erpnext");
	frappe.wiz.add_slide(schools.wiz.org);
	frappe.wiz.add_slide(schools.wiz.program);
	frappe.wiz.add_slide(schools.wiz.course);
	frappe.wiz.add_slide(schools.wiz.instructor);
	frappe.wiz.add_slide(schools.wiz.room);

});

