frappe.ready(function() {
	var form = $('form[data-web-form="discussion"]'),
		owner = form.attr('data-owner');

	var is_new = window.location.href.search("new=1")
	if(owner != frappe.session.user && is_new<0) {
		form.toggle(false);
		$('div[class="page-header-actions-block"]').toggle(false);
		
		$('<p>' + $('[name="description"]').val() + '</p>').insertBefore('.comments');
	}
	// bind events here
})