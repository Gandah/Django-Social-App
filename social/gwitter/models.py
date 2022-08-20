#django-social/social/gwitter/models.py

from venv import create
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    """
    Create a profile for each user. This will be used to store the user's rotation values.
    @param user - the user's profile           
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self",
     related_name="followed_by",
      symmetrical=False,
       blank=True)

    def __str__(self):
        return self.user.username 

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    If the user is new, Create a new profile for the user and add it to the list of profiles that the user follows.
            @param user - the user instance
            @returns the user profile      
    """
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile) #Can use .set() or .add() here but .set() requires the argument [instance.profile.id] to passed
        user_profile.save()

class Gweet(models.Model):
    user = models.ForeignKey(User, related_name="gweets", on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return(f"{self.user}"
        f"({self.created_at:%Y-%m-%d %H:%M}):"
        f"{self.body[:30]}....")


# post_save.connect(create_profile, sender=User)    
