from django.contrib import admin
from imagekit.admin import AdminThumbnail
import events

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'host', 'start_time', 'end_time',)
    # admin_thumbnail = AdminThumbnail(image_field='event_photo')
    list_filter = ('start_time',)
    search_fields = ['title', 'host', 'description']
    ordering = ('-created_at',)

admin.site.register(events.models.Event, EventAdmin)