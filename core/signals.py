from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from core.models import Profile, SimpleStore#, ListStore, MapStore

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    ''' create a profile for every user '''
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_save, sender=User)
def save_username(sender, instance, **kwargs):
    ''' modify username '''
    if instance.username is None:
        # username equal email always
    	instance.username = instance.email

# @receiver(pre_save, sender=ListStore)
# def save_member_content_type(sender, instance, **kwargs):
#     ''' modify the generic relation information on the member field '''
#     instance.content_type = get_content_type(instance)
#     instance.object_id = instance.member.id
#     instance.save()
#
# @receiver(pre_save, sender=MapStore)
# def save_member_content_type(sender, instance, **kwargs):
#     ''' modify the generic relation information on the member field '''
#     instance.content_type = get_content_type(instance)
#     instance.object_id = instance.member.id
#     instance.save()
#
# # helper functions
#
# def get_content_type(instance):
#     ''' get the ContentType for members of map and list data store objects '''
#     content_type = None
#     if instance.member is MapStore:
#         content_type = ContentType.objects.get_for_model(MapStore)
#     elif instance.member is ListStore:
#         content_type = ContentType.objects.get_for_model(MapStore)
#     else:
#         content_type = ContentType.objects.get_for_model(SimpleStore)
#     return content_type
