
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender = Profile)
def profileUpdated(sender, instance, created, **kwargs):
    print('profile Saved!')
    print("instacne:", instance)
    print('Created',created)

#@receiver(post_save, sender = Profile)
def createprofile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user, 
            username = user.username, 
            email = user.email, 
            name= user.first_name
        )

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
  


post_save.connect(createprofile, sender=User)
post_delete.connect(deleteUser, sender=Profile)