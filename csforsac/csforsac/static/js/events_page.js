
$.ajax({
    url: "/events-api",
    type: 'GET',
    success: function(events) {
		createCalendarEvents(events);
    }
});


var preparedEvents=new Array();

function createCalendarEvents(events) {
	var e;
	for (e in events) {
		preparedEvents[e] = {};
		
		//dates
		preparedEvents[e]["start"] = events[e]["start_date"] +" " +  events[e]["start_time"];
		preparedEvents[e]["end"] = events[e]["end_date"] + " " + events[e]["end_time"];
		
		preparedEvents[e]["title"] = events[e]["title"];
		
	}
	console.log(preparedEvents);
	$('.event-calendar').equinox({
  events: preparedEvents
});
}





