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

// pops up a new/existing dialog box as pulled from
// the web site
function get_dialog(div_name, url) {
    // check if the div already exists
    if ($("#dialog_container #" + div_name).length == 0) {
	alert(div_name + " doesn't exist");
	$("#dialog_container").append("<div id=" + div_name + "></div>");
    } else {
	alert(div_name + " does exist");
    }

    //in
}
