from django import forms
import subevents
from django.core.files.images import get_image_dimensions

#No clue if this actually works
class SubeventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) 
        super(SubeventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = subevents.models.Subevent
        fields = ['title', 'description', 'start_time', 'end_time',]