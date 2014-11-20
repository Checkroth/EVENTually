from django.shortcuts import render
import events

# Create your views here.
def dashboard(request):
    user = request.user
    my_events = events.models.Event.objects.filter(host=user)

    return render(request, 'static_pages/dashboard.html', {
        'user': user,
        'events': my_events,
        })