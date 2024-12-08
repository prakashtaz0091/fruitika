from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CustomUser


@receiver(pre_save, sender=CustomUser)
def handle_email_varification(sender, **kwargs):
    print("Saving new user data")



@receiver(post_save, sender=CustomUser)
def handle_email_varification(sender, **kwargs):
    print("email varification")