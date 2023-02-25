from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_avatar.png', 
                verbose_name='Profile Image', blank=True)
    description = models.TextField(max_length=500, 
                help_text='Description will help others to know more about you/organization.',
                null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    contact_details = models.CharField(max_length=200, verbose_name='Contact Details',
                    help_text='You can mention contact number, email id or social handels here.',
                    null=True, blank=True)
    is_publisher = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.user.username

class Event(models.Model):
    event_mode = [
    ('online', 'Online'),
    ('offline', 'Offline/Live'),
    ]

    event_monetized=[
    ('free', 'Free'),
    ('paid', 'Paid'),
    ]

    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    banner_img = models.ImageField(upload_to='banner_images', null=True, blank=True, verbose_name='Banner Image')
    description = models.TextField(max_length=1000)
    date_of_event = models.DateTimeField(verbose_name='Date of Event')
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    venue = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    event_mode = models.CharField(max_length=10, choices=event_mode)
    event_monetized = models.CharField(max_length=4, choices=event_monetized)
    event_cost = models.PositiveIntegerField()
    no_of_seats = models.PositiveIntegerField(verbose_name='No of seats', blank=True, null=True)

    def __str__(self):
        return self.title