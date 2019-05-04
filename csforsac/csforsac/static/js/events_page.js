const myEvents = [
      {
        start: '2019-04-20 17:30',
        end: '2019-04-20 17:30',
        title: 'CSforSAC Opening',
        url: '#',
        class: 'custom-class',
        color: '#000',
        
      },
      {
        start: '2018-05-20 17:30',
        end: '2018-05-22 17:30',
        title: 'Event 2',
        url: '#',
        class: 'custom-class',
        color: '#000',
        
      },
      {
        start: '2018-06-20 17:30',
        end: '2018-06-22 17:30',
        title: 'Event 3',
        url: '#',
        class: 'custom-class',
        color: '#000',
        
      }
]

$('.event-calendar').equinox({
  events: myEvents
});