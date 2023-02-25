from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.authtoken.models import Token

# ready method is implemented in apps.py to register the signals

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    '''
        sender - default User model
        instance - instance(row) that just got created in User model (new user is creaated in User model)
        created - created is flag(boolean), True - if 'NEW' instance got saved in moodel, False - if instance already in model and just being modified.
    '''
    if created:
        '''
            create a new user profile for each new User
        '''
        u_profile = UserProfile.objects.create(user=instance)
        u_profile.save()

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)