from django.db import models

from django.contrib.auth.models import User


# models
class Profile(models.Model):
    """ user profile to hold extra data from django's default User class """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.username + '\'s profile'
