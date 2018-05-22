//toggle over setted functions

var ids = document.querySelectorAll('[src="/EPATENT/images/open.gif"]');

// resultPage() is defined at patent detail page
if(ids.length == 0){
	var apply_number = document.getElementById("table4").innerText;
	var apply_date = document.getElementById("table5").innerText;
	var protection_type = document.getElementById("table12").innerText;
	var registration_id = document.getElementById("table15").innerText;
	var registration_date = document.getElementById("table16").innerText;
	var owner_1 = document.getElementById("table28").innerText;
	var owner_2 = document.getElementById("table29").innerText;
	var title = document.getElementById("table30").innerText;
	var summary = document.getElementById("table31").innerText;
	var ipc_codes = document.querySelector('[rowspan="5"]').innerText;
	var merged_string =
	"apply_number=" + apply_number + "END_OF_DATA"+
	"apply_date=" + apply_date + "END_OF_DATA"+
	"registration_id=" + registration_id + "END_OF_DATA"+
	"registration_date=" + registration_date + "END_OF_DATA"+
	"protection_type=" + protection_type + "END_OF_DATA"+
	"owner_1=" + owner_1 + "END_OF_DATA"+
	"owner_2=" + owner_2 + "END_OF_DATA"+
	"title=" + title + "END_OF_DATA"+
	"summary=" + summary + "END_OF_DATA"+
	"ipc_codes=" + ipc_codes + "END_OF_DATA";
	console.log(merged_string);
	resultPage();
}
else{
	if(ids.length > 0){
		//get cookie
		var index = getCookie("index");
		if(index == ""){index = 0;}
		console.log(index);
		var onClickText = ids[index].getAttribute("onclick");
		var id = onClickText.slice(28,-3);

		//set cookie of index
		setCookie("index", parseInt(index) + 1);
		viewPublication(id);
	}
}

//Functions
function setCookie(cname, cvalue) {
    document.cookie = cname + "=" + cvalue + ";";
}

function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function isFunction(fn){
    return typeof fn === "function";
}

function isDefined(fn){
    return typeof fn !== 'undefined';
}