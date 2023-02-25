from django.contrib import admin
from .models import UserProfile, Event
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_publisher')


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'date_of_event')

admin.site.register(UserProfile)
admin.site.register(Event, EventAdmin)
