

//make a get request to get an array of event objects
$.ajax({
    url: "/events-api",
    type: 'GET',
    success: function(events) {
		createCalendarEvents(events);
    }
});

//the querystring that will tell us if the user wants
//to view the map or calendar
var querystring;

$(function() {
	querystring=window.location.search.substring(1);
	if (querystring == "map") {
		selectMap();
	} else {
		selectCalendar();
	}
	console.log(querystring);
});

$("#map-option").click(function() {
	selectMap();
});

$("#calendar-option").click(function() {
	selectCalendar();

});


function showCalendar() {
	$("#event-calendar").show();
}

function hideCalendar() {
	$("#event-calendar").hide();
}

function showMap() {
	$("#event-map").show();
}

function hideMap() {
	$("#event-map").hide();
}

function selectMap() {
	showMap();
	hideCalendar();
	$("#map-option").addClass("btn-selected");
	$("#map-option").removeClass("btn-unselected");
	$("#calendar-option").addClass("btn-unselected");
	$("#calendar-option").removeClass("btn-selected");
	$("#map-option").blur();
}

function selectCalendar() {
	showCalendar();
	hideMap();
	$("#calendar-option").addClass("btn-selected");
	$("#calendar-option").removeClass("btn-unselected");
	$("#map-option").addClass("btn-unselected");
	$("#map-option").removeClass("btn-selected");
	$("#calendar-option").blur();
}
var preparedEvents=new Array();

function createCalendarEvents(events) {


	var e;
	for (e in events) {
		preparedEvents[e] = {};
		
		//dates
		preparedEvents[e]["start"] = events[e]["start_date"] +" " +  events[e]["start_time"];
		preparedEvents[e]["end"] = events[e]["end_date"] + " " + events[e]["end_time"];
		
		preparedEvents[e]["title"] = events[e]["title"];
		preparedEvents[e]["url"] = "" + events[e]["slug"];
		console.log(events);
		
	}
	console.log(preparedEvents);
	$('.event-calendar').equinox({
		events: preparedEvents
	});
}





