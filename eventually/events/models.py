import django.db.models
import django.contrib.auth
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

class Event(django.db.models.Model):
    HOST = 'HOST'
    GUESTS = 'GUESTS'
    EVERYONE = 'EVERYONE'

    INVITER_OPTIONS = (
        (HOST, 'Just me'),
        (GUESTS, 'Guests & me'),
        (EVERYONE, 'Everyone')
    )

    host = django.db.models.ForeignKey(django.contrib.auth.models.User, related_name='event_host')
    title = django.db.models.CharField(max_length=255)
    description = django.db.models.TextField(null=True, blank=True)
    event_photo = django.db.models.ImageField(upload_to='events', max_length=255, null=True, blank=True)
    start_time = django.db.models.DateTimeField()
    end_time = django.db.models.DateTimeField()
    created_at = django.db.models.DateTimeField(auto_now_add=True)
    inviter = django.db.models.CharField(max_length=255, choices=INVITER_OPTIONS, default=HOST, verbose_name='Who can invite guests')

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

    def can_invite(self, user):
        if self.inviter == self.HOST:
            return user == self.host

        if self.inviter == self.GUESTS:
            return user == self.host or self.is_invited(user) 

        return True

    # TODO: check if user is guest
    def is_invited(self, user):
        user_presence = Invite.objects.all().filter(event=self)
        if user_presence.__contains__(user):
            return True
        else:
            return False

    def get_guests(self):
        return Invite.objects.all().filter(event=self)


class Invite(django.db.models.Model):
    UNKNOWN = '?'
    YES = 'Y'
    NO = 'N'

    ATTENDING_OPTIONS = (
        (UNKNOWN, ''),
        (YES, 'Yes'),
        (NO, 'No')
    )

    event = django.db.models.ForeignKey(Event, related_name='invite_event')
    user = django.db.models.ForeignKey(django.contrib.auth.models.User, related_name='invite_user')
    attending = django.db.models.CharField(max_length=1, choices=ATTENDING_OPTIONS, default=UNKNOWN, verbose_name='Will you be attending')


# This section needs some work, its not saving instance guests addition
# def add_host(sender, instance, created, **kwargs):
#     if created:
#         instance.guests.add(instance.host)
#         instance.save()

# post_save.connect(add_host, sender=Event)
