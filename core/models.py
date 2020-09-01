from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

import jsonfield


# Constants

class DataAccessType(models.TextChoices):
    """ specifies the types of communities """
    COMMUNITY = 'PUBL', _('Public')
    USER = 'USER', _('User')
    ADMIN = 'ADMN', _('Admin')


# Models

class Feature(models.Model):
    """ features built by 3rd party developers """
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='feature_pictures/')
    description = models.TextField()

    # used to validate
    key = models.CharField(max_length=10, unique=True)

    payload = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='features')

    approved = models.NullBooleanField()

    class Meta:
        ordering = ['id']

    def get_random_key(self):
        """ generate a random key """
        _key = User.objects.make_random_password(length=10, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

        # check if the key already exists in another community and generate another
        if Feature.objects.filter(key=_key).exists():
            return self.get_random_key()

        return _key

    def save(self, *args, **kwargs):
        """ override the default save function """

        # check if the object is being created
        if not self.id:
            # assign the key
            self.key = self.get_random_key()

        # call the parent save
        super(Feature, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class CommunityType(models.Model):
    """ represents community types """
    value = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.value


class Community(models.Model):
    """ communities which organisations create """
    name = models.CharField(max_length=32)
    type = models.ForeignKey(
        CommunityType, on_delete=models.SET_DEFAULT, default=1, related_name='communities_with_type')
    picture = models.ImageField(upload_to='community_pictures/')
    description = models.TextField(default='')

    # determines if the community can be joined by anyone or only by people with the key
    # is_public = models.BooleanField(default=False)

    # used to join the community if it is not public
    key = models.CharField(max_length=10, unique=True)

    # django automatically creates the relationship model for many-to-many fields
    admins = models.ManyToManyField(User, related_name='communities_admined', blank=True)
    members = models.ManyToManyField(User, related_name='communities_joined', blank=True)

    features = models.ManyToManyField(Feature, related_name='communities_using', blank=True)

    class Meta:
        verbose_name_plural = 'communities'
        ordering = ['id']

    # used twice. abstract to method?
    def get_random_key(self):
        """ generate a random key """
        _key = User.objects.make_random_password(length=10, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

        # check if the key already exists in another community and generate another
        if Community.objects.filter(key=_key).exists():
            return self.get_random_key()

        return _key

    def save(self, *args, **kwargs):
        """ override the default save function """

        # check if the object is being created
        if not self.id:
            # assign the key
            self.key = self.get_random_key()

        # call the parent save
        super(Community, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def is_admin_or_member(self, user):
        if user in self.admins.all():
            return True
        if user in self.members.all():
            return True
        return False

    def is_admin(self, user):
        if user in self.admins.all():
            return True
        return False

    def get_community_type_value(self):
        return self.type.value


# datastore models

class SimpleStore(models.Model):
    """ simple data store for features """
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='simple_store')

    key = models.CharField(max_length=128)
    value = jsonfield.JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simple_store')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='simple_store')

    access = models.CharField(max_length=32, choices=DataAccessType.choices)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.feature.name + '\'s simple store'


class UploadedImage(models.Model):
    """ stores uploaded images via features """

    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return 'Image'