import django.db.models
import events
import django.contrib.auth
# Create your models here.

class Subevent(django.db.models.Model):
    main_event = django.db.models.ForeignKey(events.models.Event)
    host = django.db.models.ForeignKey(django.contrib.auth.models.User)
    title = django.db.models.CharField(max_length=255)
    description = django.db.models.TextField(null=True, blank=True)
    # Guest list for subevents necessary?

    def save(self, *args, **kwargs):
        if not self.pk and not self.host and self.main_event:
            self.host = main_event.host
        super(Subevent, self).save(*args, **kwargs)
