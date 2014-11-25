import django.db.models
import django.contrib.auth
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

class Event(django.db.models.Model):
    host = django.db.models.ForeignKey(django.contrib.auth.models.User, related_name='event_host')
    title = django.db.models.CharField(max_length=255)
    description = django.db.models.TextField(null=True, blank=True)
    guests = django.db.models.ManyToManyField(django.contrib.auth.models.User, related_name='event_guests', null=True, blank=True)
    event_photo = django.db.models.ImageField(upload_to='events', max_length=255, null=True, blank=True)
    start_time = django.db.models.DateTimeField()
    end_time = django.db.models.DateTimeField()
    created_at = django.db.models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def subevents(self):
        return self.subevent_set.all()

    def save(self, *args, **kwargs):
        if self.start_time < self.end_time:
            super(Event, self).save(*args, **kwargs)
        else:
            raise ValidationError('Start time must be earlier than end time.')

    def get_absolute_url(self):
        #Allows an event to give its own unique url to the views/templates
        return reverse('show_event', kwargs={'event_id': self.pk})


# This section needs some work, its not saving instance guests addition
# def add_host(sender, instance, created, **kwargs):
#     if created:
#         instance.guests.add(instance.host)
#         instance.save()

# post_save.connect(add_host, sender=Event)
