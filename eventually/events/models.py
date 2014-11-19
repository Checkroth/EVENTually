import django.db.models
import django.contrib.auth

class Event(django.db.models.Model):
    host = django.db.models.ForeignKey(django.contrib.auth.models.User, related_name='event_host')
    title = django.db.models.CharField(max_length=255)
    description = django.db.models.TextField(null=True, blank=True)
    guests = django.db.models.ManyToManyField(django.contrib.auth.models.User, related_name='event_guests')

    def subevents(self):
        return self.subevent_set.all()

    def save(self, *args, **kwargs):
        if not self.pk and self.host:
            guests.add(self.host)
        super(Event, self).save(*args, **kwargs)