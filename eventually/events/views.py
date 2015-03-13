from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import events
import events.forms

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
        'events': my_events,
        })

def my_events_json(request):
    try:
        user = request.user
        my_events = events.models.Event.objects.all().filter(host=user)
    except:
        user = {'username': 'no user',}
        my_events = []

    data = serializers.serialize('json', my_events)
    return HttpResponse(data, 'application/json')

def create_event(request):
    if request.POST:
        form = events.forms.EventForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            event = form.save(False)
            event.host = user
            event.save()
            return redirect('{}'.format(event.get_absolute_url()))
    else:
        form = events.forms.EventForm(initial={'host': request.user})
    return render(request, 'events/create_event.html', {
        'form': form,
        })

def show_event(request, event_id):
    event = events.models.Event.objects.get(id=event_id)
    return render(request, 'events/main_event.html', {
        'event': event,
        })
    # Need to do the url based jangles here