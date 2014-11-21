from django import forms
import events

class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EventForm, self).__init__(*args, **kwargs)

    class Meta:
        model = events.models.Event
        fields = ['title', 'description', 'event_photo', 'start_time', 'end_time',]


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


#Example of image size validation, will be necessary at a later time.

# from django.core.files.images import get_image_dimensions
# class myForm(forms.ModelForm):
#    class Meta:
#        model = myModel
#    def clean_picture(self):
#        picture = self.cleaned_data.get("picture")
#        if not picture:
#            raise forms.ValidationError("No image!")
#        else:
#            w, h = get_image_dimensions(picture)
#            if w != 100:
#                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
#            if h != 200:
#                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
#        return picture