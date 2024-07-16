from django.db import models
from django .contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user=models.OneToOneField(User , on_delete=models.CASCADE)
    address = models.CharField(help_text = "text",max_length = 150)
    phone=models.IntegerField(default=1)
    

    def __str__(self)  :
        return str (self.user)
    

        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)        
        