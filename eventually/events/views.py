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