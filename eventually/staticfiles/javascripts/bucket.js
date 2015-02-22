$(document).ready(function() {

    // CALENDAR

    $('#calendar').fullCalendar({
        header: {
				left: 'prev,next today',
				center: 'title',
				right: 'month,agendaWeek,agendaDay'
			},
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        timezone: 'UTC',
        events: function(start, end, timezone, callback) {
            $.ajax({
                url: 'my_events_json',
                dataType: 'json',
                success: function(events) {
                    debugger;
                    callback(events.map(function (e) {
                        return {
                            title: e.fields.title,
                            start: $.fullCalendar.moment(e.fields.start_time),
                            end: $.fullCalendar.moment(e.fields.end_time)
                        };
                    }));
                }
            });
        }

    })
    
    // EVENT SCROLLER
    
     $("#scroller").simplyScroll({
        	   auto: false,
			 speed: 5
     });
    
    // SIDR MOBILE NAV
    
    $('#sidr-menu').sidr();	
    $('#sidr-menu').click(function(){
	   var $this = $('body'); //has to be the container of all the content which may differ per design
		  if( $this.is('.fixed') ) {
	           $this.removeClass('fixed');
	       }
	       else {
		      $this.addClass('fixed');
	       }
	   });	
	   
    
});


                 
