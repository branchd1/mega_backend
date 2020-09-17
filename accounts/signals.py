""" This module hold signals related to authentication and profile """

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from accounts.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a profile for every user

    Parameters
    ----------
    sender
    instance
    created
    kwargs

    Returns
    -------
    None

    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Update profile when user is updated

    Parameters
    ----------
    sender
    instance
    kwargs

    Returns
    -------
    None

    """
    instance.profile.save()


@receiver(pre_save, sender=User)
def save_username(sender, instance, **kwargs):
    """
    Set username when user is created

    Parameters
    ----------
    sender
    instance
    kwargs

    Returns
    -------
    None

    """
    if instance.username == '':
        # username equal email always
        instance.username = instance.email
        instance.save()
