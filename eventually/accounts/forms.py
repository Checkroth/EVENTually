from django import forms
import django.contrib.auth.models
import accounts
from django.core.files.images import get_image_dimensions

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

    class Meta:
        model = django.contrib.auth.models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }
