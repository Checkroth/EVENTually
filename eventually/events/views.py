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
    try:
        user = request.user
    except:
        user = {'username': 'no user',}

    event = events.models.Event.objects.get(id=event_id)
    invite_form = events.forms.InviteForm()
    return render(request, 'events/main_event.html', {
        'event': event,
        'can_invite': event.can_invite(user),
        'invite_form': invite_form
        })

def invite(request, event_id):
    event = events.models.Event.objects.get(id=event_id)

    if request.POST:
        form = events.forms.InviteForm(request.POST)
        invite = form.save(False)
        invite.event = event
        invite.save()

def event_inbox(request):
    try:
        user = request.user
    except:
        user = {'username': 'no user',}

    usersInvites = events.models.Invite.objects.all().filter(user=user)

    return render(request, 'events/event_inbox.html', {
        'invites' : usersInvites
        })

def event_inbox_json(request):
    try:
        user = request.user
        invites = events.models.Invite.objects.all().filter(user=user)
    except:
        user = {'username': 'no user',}
        invites = []

    data = serializers.serialize('json', invites)
    return HttpResponse(data, 'application/json')

    return redirect('{}'.format(event.get_absolute_url()))
