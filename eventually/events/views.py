from django.shortcuts import render
import events

# Create your views here.
def my_events(request):
    user = request.user
    my_events = events.models.Event.objects.all().filter(host=user)

    return render(request, 'events/my_events.html', { 
        'user': user,
        'events': my_events
        })