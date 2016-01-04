$(document).ready(function() {    
    $("#login_btn").click(function() {
        var me = this;
        $(this).html("Logging In...").prop("disabled", true);
        frappe.call({
            "method": "login",
            args: {
                usr: "demo@erpnext.com",
                pwd: "demo",
                lead_email: $("#lead-email").val(),
            },
            callback: function(r) {
                $(me).prop("disabled", false);
                if(r.exc) {
                    alert("Error, please contact support@erpnext.com");
                } else {
                    console.log("Logged In");
                    window.location.href = "desk";
                }
            }
        })
        return false;
    })
    .prop("disabled", false);
})
