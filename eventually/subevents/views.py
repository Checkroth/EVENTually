from django.shortcuts import render
import events
import subevents

# Create your views here.

# Need login required flag here
def create_subevent(self, event_id):
	main_event = events.models.Event.objects.get(id=event_id)
	if request.user is not main_event.host:
		# Need more logic for subevent hosts who are not main event hosts (ManyToManyField?)
		#We obviously need a redirect page here
		return HttpResonse(request, 'http://www.google.com')

	if request.POST:
		form = subevents.forms.SubeventForm(request.POST, request.FILES)
		if form.is_valid():
			user = request.user
			subevent = form.save(False)
			# subevent.host = user
			subevent.save()
			return redirect('{}'.format(subevent.get_absolute_url()))
	else:
		form = subevents.forms.SubeventForm(initial={
			'host': request.user,
			'main_event__id': event_id,
			})
	return render(request, 'subevents/create_subevent.html', {
		'form': form,
		})

def show_subevent(request, subevent_id):
	subevent = subevents.models.Subevent.objects.get(id=subevent_id)
	return render(request, 'subevents/_subevent.html', {
		'subevent': subevent,
		})
	