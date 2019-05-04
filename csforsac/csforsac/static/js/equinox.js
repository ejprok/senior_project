/**
 * jQuery Equinox v1.0.0
 * Copyright 2014 Jordan Crown
 * Contributing Author: Cameron Rahman
 */

/* global moment */

(function($) {

	var defaultSettings = {
		events: [],
		// queryUrl: null,
		detailedWidthBreakpoint: 550,
		onEventClick: null,
		onPreviousMonthStart: null,
		onNextMonthStart: null,
		onCurrentMonthStart: null,
		onLoadStart: null,
		onLoadEnd: null
	};

	var defaultEventSettings = {
		start: null,
		end: null,
		title: '',
		url: '',
		class: '',
		color: '',
		data: {}
	};

	var methods = {
		init: function(options) {
			return this.each(function() {
				var $this = $(this);
				var data = $this.data('equinox');

				if(!data) {
					var settings = $.extend({}, defaultSettings, options);

					var currentDate = moment();

					var validEvents = [];
					for(var i = 0; i < settings.events.length; i++) {
						settings.events[i] = $.extend({}, defaultEventSettings, settings.events[i]);

						settings.events[i].start = moment(settings.events[i].start);
						settings.events[i].end = moment(settings.events[i].end);

						if(!settings.events[i].start.isValid() || !settings.events[i].end.isValid()) continue;
						if(settings.events[i].start.valueOf() > settings.events[i].end.valueOf()) continue;

						settings.events[i].allDay = isAllDay(settings.events[i].start, settings.events[i].end);
						settings.events[i].daySpan = getDaySpan(settings.events[i].start, settings.events[i].end);

						validEvents.push(settings.events[i]);
					}
					settings.events.sort(function(a, b) { return a.start.valueOf() - b.start.valueOf(); });

					// segment events into start dates
					var segmentedEvents = [];
					for(var i = 0; i < settings.events.length; i++) {
						settings.events[i].id = i;
						var key = moment(settings.events[i].start).startOf('day').format('UX');
						if(!(key in segmentedEvents)) {
							segmentedEvents[key] = [];
						}
						segmentedEvents[key].push(settings.events[i]);
					}

					// save object data
					data = {
						target: $this,
						settings: settings,
						currentDate: currentDate,
						segmentedEvents: segmentedEvents,
						activeMonth: moment(currentDate).startOf('month')
					};
					$this.data('equinox', data);

					$this.addClass('equinox');

					// output initial calendar view
					$this.equinox('refresh');
					$this.equinox('load');

					$(window).resize(function() {
						$this.equinox('refresh');
					});

					$this.on('click', '.calendar-actions button.prev', function(e) {
						var data = $this.data('equinox');
						data.activeMonth.subtract(1, 'months');
						if(typeof(data.settings.onPreviousMonthStart) === typeof(Function)) {
							data.settings.onPreviousMonthStart(e, data);
						}
						$this.equinox('load');
					});

					$this.on('click', '.calendar-actions button.next', function(e) {
						var data = $this.data('equinox');
						data.activeMonth.add(1, 'months');
						if(typeof(data.settings.onNextMonthStart) === typeof(Function)) {
							data.settings.onNextMonthStart(e, data);
						}
						$this.equinox('load');
					});

					$this.on('click', '.calendar-actions button.today', function(e) {
						var data = $this.data('equinox');
						var currentMonth = moment().startOf('month');
						if(typeof(data.settings.onCurrentMonthStart) === typeof(Function)) {
							data.settings.onCurrentMonthStart(e, data);
						}
						if(data.activeMonth.startOf('month').diff(currentMonth) !== 0) {
							data.activeMonth = currentMonth;
							$this.equinox('load');
						}
					});

					$this.on('click', 'a.event', function(e) {
						var data = $this.data('equinox');
						if(typeof(data.settings.onEventClick) === typeof(Function)) {
							var eventObject = data.settings.events[$(this).data('event-id')];
							var eventData = $.extend({
								start: eventObject.start,
								end: eventObject.end,
								title: eventObject.title,
								url: eventObject.url,
								class: eventObject.class
							}, eventObject.data);
							data.settings.onEventClick(e, eventData);
						}
					});

				}
			});
		},
		load: function() {
			return this.each(function() {
				var $this = $(this);
				var data = $this.data('equinox');

				if(typeof(data.settings.onLoadStart) === typeof(Function)) {
					data.settings.onLoadStart(data);
				}
				
				var activeMonth = data.activeMonth;
				var calendar = getMonthHtml(activeMonth, data.segmentedEvents);

				if(typeof(data.settings.onLoadEnd) === typeof(Function)) {
					data.settings.onLoadEnd(data);
				}

				$this.html(calendar);

			});
		},
		refresh: function() {
			return this.each(function() {
				var $this = $(this);
				var data = $this.data('equinox');

				if($this.width() < data.settings.detailedWidthBreakpoint) {
					$this.removeClass('detailed');
				} else {
					$this.addClass('detailed');
				}

			});
		}
	};

	$.fn.equinox = function(method) {
		if(methods[method]) {
			return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
		} else if(typeof method === 'object' || !method) {
			return methods.init.apply(this, arguments);
		} else {
			$.error('Method ' +  method + ' does not exist on jQuery.equinox');
		}
	};



	var getMonthHtml = function(month, events) {

		var monthHtml = $('<div class="calendar"></div>');
		
		var header = $('<div class="calendar-header"></div>');
		header.append('<div class="month-label">' + month.format('MMMM YYYY') + '</div>');
		header.append('<div class="calendar-actions"></div>');
		$('.calendar-actions', header).append('<button type="button" class="prev">Previous</button> ');
		$('.calendar-actions', header).append('<button type="button" class="next">Next</button> ');
		$('.calendar-actions', header).append('<button type="button" class="today">Today</button> ');
		monthHtml.append(header);

		var weeks = $('<div class="month-weeks"></div>');

		var weekHeader = $('<div class="week week-header"><div class="days-container"></div></div>');
		for(var i = 0; i < 7; i++) {
			$('.days-container', weekHeader).append('<div class="day ' + moment().day(i).format('dddd').toLowerCase() + '">' + moment().day(i).format('dddd') + '</div>');
		}
		weeks.append(weekHeader);

		var date = moment(month).startOf('month').startOf('week');

		// build initial leftovers array from previous month
		var leftovers = [];
		for(var i in events) {
			if(parseInt(i.substr(1)) >= date.unix()) break;
			for(var j = 0; j < events[i].length; j++) {
				if(events[i][j].end.valueOf() > date.valueOf()) {
					events[i][j].daysLeft = getDaySpan(date, events[i][j].end) - (isMidnight(events[i][j].end) ? 1 : 0);
					leftovers.push(events[i][j]);
				}
			}
		}
		
		var endOfMonthReached = false;
		var daysInMonth = month.daysInMonth();
		var currentDate = moment();
		for(i = 0; !endOfMonthReached; i++) {
			var week = $('<div class="week week-' + i + '"></div>');


			var weekEventSlots = [[]];
			var weekDate = moment(date);
			for(var j = 0; j < 7; j++) {
				weekDate.day(j);

				// add leftovers from previous week
				if(j === 0) {
					for(var k = 0; k < leftovers.length; k++) {
						var slot = 0;
						while(weekEventSlots[slot][j]) {
							slot++;
							if(!(slot in weekEventSlots)) weekEventSlots[slot] = [];
						}
						weekEventSlots[slot][j] = leftovers[k];
						for(var l = j + 1; l < leftovers[k].daysLeft + j && l < 7; l++) {
							weekEventSlots[slot][l] = 'reserved';
						}
					}
				}

				var dateEvents = (weekDate.format('UX') in events) ? events[weekDate.format('UX')] : [];
				for(var k = 0; k < dateEvents.length; k++) {
					if(dateEvents[k].daySpan < 2) continue;
					var slot = 0;
					while(weekEventSlots[slot][j]) {
						slot++;
						if(!(slot in weekEventSlots)) weekEventSlots[slot] = [];
					}
					dateEvents[k].daysLeft = dateEvents[k].daySpan - (isMidnight(dateEvents[k].end) ? 1 : 0);
					weekEventSlots[slot][j] = dateEvents[k];
					for(var l = j + 1; l < dateEvents[k].daysLeft + j && l < 7; l++) {
						weekEventSlots[slot][l] = 'reserved';
					}
				}
			}

			leftovers = [];
			week.append('<ul class="week-events"></ul>');
			for(var j = 0; j < weekEventSlots.length; j++) {
				var slot = $('<li class="slot"><ul></ul></li>');
				for(var k = 0; k < 7; k++) {
					if(weekEventSlots[j][k] === 'reserved') {
						continue;
					} else if(!weekEventSlots[j][k]) {
						$('ul', slot).append('<li class="event-container"></li>');
					} else {
						var eventContainer = $('<li class="event-container span-' + Math.min(weekEventSlots[j][k].daysLeft, 7 - k) + '"></li>');
						if(weekEventSlots[j][k].daySpan - (isMidnight(weekEventSlots[j][k].end) ? 1 : 0) > weekEventSlots[j][k].daysLeft) eventContainer.addClass('continuation');
						if(weekEventSlots[j][k].daysLeft > 7 - k) eventContainer.addClass('continued');
						eventContainer.append(getEventHtml(weekEventSlots[j][k]));
						$('ul', slot).append(eventContainer);
						if(weekEventSlots[j][k].daysLeft > 7 - k) {
							weekEventSlots[j][k].daysLeft -= 7 - k;
							leftovers.push(weekEventSlots[j][k]);
						} else {
							delete weekEventSlots[j][k].daysLeft;
						}
					}
				}
				$('.week-events', week).append(slot);
			}


			week.append('<div class="days-container"></div>');
			for(var j = 0; j < 7; j++) {
				date.day(j);

				var reservedSlots = [];
				for(var k = 0; k < weekEventSlots.length; k++) {
					if(weekEventSlots[k][j]) {
						reservedSlots.push(k);
					}
				}

				var dateEvents = (date.format('UX') in events) ? events[date.format('UX')] : [];

				$('.days-container', week).append(getDateHtml(date, dateEvents, reservedSlots, month, currentDate));

				if(date.month() === month.month() && date.date() === daysInMonth) {
					endOfMonthReached = true;
				}

			}

			weeks.append(week);
			date.add(1, 'days'); // increment to next week
		}

		monthHtml.append(weeks);

		return monthHtml;

	};

	var getDateHtml = function(date, events, reservedSlots, activeMonth, currentDate) {

		var dateClasses = [
			'date',
			'date-' + date.date(),
			'day',
			moment(date).format('dddd').toLowerCase()
		];
		if(date.month() !== activeMonth.month()) {
			dateClasses.push('outside-month');
		}
		if(moment(date).startOf('day').valueOf() === moment(currentDate).startOf('day').valueOf()) {
			dateClasses.push('current-date');
		}
		if(events.length || reservedSlots.length) {
			dateClasses.push('has-events');
		}

		var dateHtml = $('<div class="' + dateClasses.join(' ') + '"></div>');
		dateHtml.append('<div class="date-label">' + (date.date() === 1 ? date.format('MMM ') : '') + date.date() + '</div>');
		dateHtml.append('<ul class="date-events"></ul>');

		var slot = 0;
		var reservedSlot = reservedSlots.shift();
		for(var i = 0; i < events.length; i++) {
			if(slot === reservedSlot) {
				$('.date-events', dateHtml).append('<li class="event-container placeholder"></li>');
				reservedSlot = reservedSlots.shift();
				i--;
			} else if(events[i].daySpan >= 2) {
				continue;
			} else {
				var eventContainer = $('<li class="event-container"></li>');
				eventContainer.append(getEventHtml(events[i]));
				$('.date-events', dateHtml).append(eventContainer);
			}
			slot++;
		}

		return dateHtml;

	};

	var getEventHtml = function(event) {

		var eventHtml = $('<a class="event ' + event.class + '" href="' + event.url + '" ' + (event.color != '' ? 'style="border-color: ' + event.color + ';"' : '') + '></a>');
		eventHtml.data('event-id', event.id);
		eventHtml.append('<span class="start-time">' + event.start.format(event.start.minutes() === 0 ? 'ha' : 'h:mma') + '</span>');
		eventHtml.append('<span class="title">' + event.title + '</span>');
		return eventHtml;

	};

	var isAllDay = function(start, end) {
		return end.diff(start) % moment.duration(1, 'days').asMilliseconds() === 0;
	};

	var isMidnight = function(time) {
		return time.format('HH:mm:ss.SSS') === '00:00:00.000';
	};

	var getDaySpan = function(start, end) {
		var startDate = moment(start).startOf('day');
		var endDate = moment(end).startOf('day');
		return (endDate.diff(startDate) / moment.duration(1, 'days').asMilliseconds()) + 1;
	};



})(jQuery);