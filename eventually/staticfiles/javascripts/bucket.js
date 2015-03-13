$(document).ready(function() {

<<<<<<< HEAD
=======
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
                    callback(events.map(function (e) {
                        return {
                            url: "event/" + e.pk,
                            title: e.fields.title,
                            start: $.fullCalendar.moment(e.fields.start_time),
                            end: $.fullCalendar.moment(e.fields.end_time)
                        };
                    }));
                }
            });
        },
        eventClick: function (calEvent) {
            window.location.href = calEvent.url;
        }

    })
    
    // EVENT SCROLLER
    
     $("#scroller").simplyScroll({
        	   auto: false,
			 speed: 5
     });
>>>>>>> master
    
    // SIDR MOBILE NAV
    
    //$('#sidr-menu').sidr();	
    //$('#sidr-menu').click(function(){
	  // var $this = $('body'); //has to be the container of all the content which may differ per design
		//  if( $this.is('.fixed') ) {
	      //     $this.removeClass('fixed');
	       //}
	       //else {
		     // $this.addClass('fixed');
//	       }
//	   });
    
    $('header nav').meanmenu({
        meanScreenWidth: "768"
    });
	   
    
});


                 
