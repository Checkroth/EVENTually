from django import forms
import events
from django.core.files.images import get_image_dimensions

#No clue if this actually works
class SubEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        super(SubEventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = events.models.Event
        fields = ['title', 'description', 'start_time', 'end_time',]