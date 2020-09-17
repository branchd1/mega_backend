""" This module contains the database models """

from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

from django.contrib.postgres.fields import JSONField


# Helper functions
def get_random_key(obj) -> str:
    """
    Generate a random key

    Returns
    -------
    str
        a unique 10 character key which a Feature object can use for its key attribute

    """
    _key = User.objects.make_random_password(length=10, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

    # check if the key already exists in another object and generate another
    if obj.__class__.objects.filter(key=_key).exists():
        return get_random_key(obj)

    return _key


# Constants

class DataAccessType(models.TextChoices):
    """
    Specifies the types of data access levels available in the simple store

    Attributes
    ----------
    COMMUNITY : str
        signifies that simple store instance is accessible to every member of a community
    USER : str
        signifies that simple store instance is only accessible to user who created it
    ADMIN : str
        signifies that simple store instance is only accessible to admin and user who created it

    """
    COMMUNITY = 'PUBL', _('Public')
    USER = 'USER', _('User')
    ADMIN = 'ADMN', _('Admin')


# Models

class Feature(models.Model):
    """
    Represents features built by 3rd party developers

    Attributes
    ----------
    name : str
        The name of the feature
    picture : object
        The picture representing the feature in UIs
    desription : str
        The description of the feature
    key : str
        A unique secret key used by feature developers to access the feature
    payload : str
        The code that instructs the frontend what components to display
    User : object
        The user who owns the feature
    approved : bool
        True if the feature has been accepted to be displayed on the frontend by the admin,
        False if rejected, and None otherwise

    """

    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='feature_pictures/')
    description = models.TextField()
    key = models.CharField(max_length=10, unique=True)
    payload = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='features')
    approved = models.NullBooleanField()

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs) -> None:
        # check if the object is being created
        if not self.id:
            # assign the key
            self.key = get_random_key(self)

        # call the parent save
        super(Feature, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class CommunityType(models.Model):
    """
    Represents community types.
    It is used in Community model to specify the type

    Attributes
    ----------
    value : str
        Human readable string that signifies the type of community

    """

    value = models.CharField(max_length=32, unique=True)

    def __str__(self) -> str:
        return self.value


class Community(models.Model):
    """
    Represents communities which are created by organisations

    Attributes
    ----------
    name : str
        The name of the community
    type : CommunityType
        An instance of CommunityType representing the community's type
    picture : object
        Image representing the community in UIs
    description : str
        A detailed description of the the community
    key : str
        A unique secret key used to gain access to the community
    admins : complex
        The admins of the community
    members : complex
        The members of the community
    features : complex
        The features which the admins have added to the community

    """

    name = models.CharField(max_length=32)
    type = models.ForeignKey(
        CommunityType, on_delete=models.SET_DEFAULT, default=1, related_name='communities_with_type')
    picture = models.ImageField(upload_to='community_pictures/', null=True)
    description = models.TextField(default='')

    # used to join the community
    key = models.CharField(max_length=10, unique=True)

    # django automatically creates the relationship model for many-to-many fields
    admins = models.ManyToManyField(User, related_name='communities_admined', blank=True)
    members = models.ManyToManyField(User, related_name='communities_joined', blank=True)

    features = models.ManyToManyField(Feature, related_name='communities_using', blank=True)

    class Meta:
        verbose_name_plural = 'communities'
        ordering = ['id']

    def save(self, *args, **kwargs) -> None:
        # check if the object is being created
        if not self.id:
            # assign the key
            self.key = get_random_key(self)

        # call the parent save
        super(Community, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def is_admin_or_member(self, user: User) -> bool:
        """
        Checks that the parameter user is a member or an admin of the community

        Parameters
        ----------
        user : object
            A user that is being checked for membership in the community

        Returns
        -------
        bool
            True if the user is a member or an admin, False if the user is neither a member or an admin

        """
        if user in self.admins.all():
            return True
        if user in self.members.all():
            return True
        return False

    def is_admin(self, user: User) -> bool:
        """
        Checks that the parameter user is an admin of the community

        Parameters
        ----------
        user : object
            A user that is being checked for admin membership in the community

        Returns
        -------
        bool
            True if the user is an admin, False if the user is not an admin

        """
        if user in self.admins.all():
            return True
        return False

    def get_community_type_value(self) -> str:
        """
        Get the value of the community's type

        Returns
        -------
        str
            A string representing the communities type value

        """
        return self.type.value


# datastore models

class SimpleStore(models.Model):
    """
    Simple data store for features

    Attributes
    ----------
    feature : Feature
        The feature responsible for the stored data
    key : str
        String used to retrieve value from the SimpleStore
    value : complex
        Json representing data stored in the data store
    user : User
        The user who stored the data
    community : Community
        The community the data is associated with
    access : enumerate
        The access level of the SimpleStore
    date : object
        The time the store was last updated

    """
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='simple_store')

    key = models.CharField(max_length=128)
    value = JSONField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simple_store')
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='simple_store')

    access = models.CharField(max_length=32, choices=DataAccessType.choices)

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.feature.name + '\'s simple store'


class UploadedImage(models.Model):
    """
    Stores images uploaded via features

    Attributes
    ----------
    image : object
        The image stored

    """

    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return 'Image'
