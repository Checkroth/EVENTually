from django import forms
import events
from django.core.files.images import get_image_dimensions

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = events.models.Event
        fields = ['title', 'description', 'event_photo', 'start_time', 'end_time',]
        widgets = {
            'start_time': forms.SplitDateTimeWidget(),
            'end_time': forms.SplitDateTimeWidget()
        }

    def clean_picture(self):
        picture = self.cleaned_data.get('event_photo')
        if not picture:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(picture)
            if w < 100:
                raise forms.ValidationError("The image must be at least 100x100. The width of this image is {}".format(w))
            if h < 100:
                raise forms.ValidationError("The image must be at least 100x100. The height of this image is {}".format(h))
        return picture



        # Widget examples

        #     labels = {
        #     'name': _('Writer'),
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }