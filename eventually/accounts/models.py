import django.db.models
import django.contrib.auth.models
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(django.db.models.Model):
    user = django.db.models.OneToOneField(django.contrib.auth.models.User) #This isn't working with super user?
    birthday = django.db.models.DateTimeField()
    join_date = django.db.models.DateTimeField(auto_now_add=True)
    profile_picture = django.db.models.ImageField(upload_to='accounts', max_length=255, null=True, blank=True)
    #interests = django.db.models.ForeignKeyField(eventually.models.interests)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

#post_save.connect(create_user_profile, sender=django.contrib.auth.models.User)