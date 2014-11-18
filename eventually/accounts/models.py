import django.db.models
import django.contrib.auth.models

# Create your models here.
class UserProfile(django.db.models.Model):
    user = django.db.models.OneToOneField(django.contrib.auth.models.User) #This isn't working with super user?
    first_name = django.db.models.CharField(max_length=100)
    last_name = django.db.models.CharField(max_length=100)
    birthday = django.db.models.DateTimeField()
    join_date = django.db.models.DateTimeField(auto_now_add=True)

    #interests = django.db.models.ForeignKeyField(eventually.models.interests)