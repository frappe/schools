cur_frm.cscript.refresh = function() {
	if(!this.frm.doc.__islocal) {
		this.frm.add_custom_button(__("Create Student"), this.create_student, "btn-default");
	}
}

this.create_customer = function() {
	console.log("ok")
}