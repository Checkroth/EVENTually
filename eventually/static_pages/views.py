from django.shortcuts import render
from django.shortcuts import redirect
import events

# Create your views here.
def dashboard(request):
    try:
        user = request.user
        my_events = events.models.Event.objects.filter(host=user)
        suggested_events = events.models.Event.objects.filter(host!=user)
    except:
        return redirect('/accounts/login')

    return render(request, 'static_pages/dashboard.html', {
        'user': user,
        'events': my_events,
        'suggested_events': suggested_events,
        })

def about(request):
    return render(request, 'static_pages/about.html')