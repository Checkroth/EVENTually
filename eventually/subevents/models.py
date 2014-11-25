import django.db.models
import events
import django.contrib.auth
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

class Subevent(django.db.models.Model):
    main_event = django.db.models.ForeignKey(events.models.Event)
    host = django.db.models.ForeignKey(django.contrib.auth.models.User)
    title = django.db.models.CharField(max_length=255)
    description = django.db.models.TextField(null=True, blank=True)
    start_time = django.db.models.DateTimeField()
    end_time = django.db.models.DateTimeField()
    created_at = django.db.models.DateTimeField(auto_now_add=True)
    # Guest list for subevents necessary?

    def save(self, *args, **kwargs):
    	# Ensure that the subevent is within the constraints of the main event. This may have to be done in the form class.
        if self.start_time > self.end_time:
        	raise ValidationError('Start time must be earlier than end time')
        if self.start_time < main_event.start_time:
        	raise ValidationError('Subevent must start within the main event\'s timeframe.')
        if self.end_time > main_event.end_time:
        	raise ValidationError('Subevent must end within the main event\'s timeframe')
        super(Subevent, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_subevent', kwargs={
            'event_id': main_event.pk,
            'subevent_id': self.pk,
            })