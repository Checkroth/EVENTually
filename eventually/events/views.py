from django.shortcuts import render
import events

# Create your views here.
def my_events(request):
    try:
    	user = request.user
    	my_events = events.models.Event.objects.all().filter(host=user)
    except:
    	user = {'username': 'no user',}
    	my_events = []

    return render(request, 'events/my_events.html', { 
        'user': user,
        'events': my_events
        })

def create_event(request):
    if request.POST:
        form = events.forms.EventForm(request.POST, request.FILES)
        if form.is_valid():
            # Need to figure out the urls for rendering events based on id, then pull it in this render
            return render(request, 'events/_event.html/{}').format(1)
    else:
        form = events.forms.EventForm(initial={'host'=request.user})
    return render(request, 'events/create_event.html', {
        'form': form,
        })

def show_event(request, event_id):
    event = events.models.Event.objects.get_or_404(id=event_id)
    return render(request, 'events/_event.html', {
        'event': event,
        })
    # Need to do the url based jangles here