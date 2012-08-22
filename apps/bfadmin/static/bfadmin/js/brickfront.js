function get_resource(name) {
    $.ajax({
	url: "/api/" + name + "/",
	success: function(data) {
	    if ("html" in data) {
		$("section#main").html(data["html"]);
	    }
	}
    });
}