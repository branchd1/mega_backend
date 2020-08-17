from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Constants

class CommunityType(models.TextChoices):
	''' specifies the types of communities '''
	BAR = 'BAR', _('Bar')
	RESTAURANT = 'RES', _('Restaurant')
	CLUB = 'CLB', _('Club')
	RELIGIOUS_INSTITUTION = 'REI', _('Religious institution')
	OFFICE = 'OFF', _('Office')
	SUPERMARKET = 'SMT', _('Supermarket')
	CINEMA = 'CNA', _('Cinema')
	HOSPITAL = 'HOS', _('Hospital')
	HOTEL = 'HTL', _('Hotel')
	RETAIL_STORE = 'RSE', _('Retail store')
	ESTATE = 'EST', _('Estate')
	PRO_SERVICES = 'PRS', _('Professional services')
	E_COM = 'ECO', _('eCommerce')
	SCHOOL = 'SCH', _('School')
	ENTERTAINMENT = 'ENT', _('Entertainment')

class DataAccessType(models.TextChoices):
	''' specifies the types of communities '''
	PUBLIC = 'PUBL', _('Public')
	USER = 'USER', _('User')

# Models

class Profile(models.Model):
	''' user profile to hold extra data from django's default User class '''
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
	phone_number = models.CharField(max_length=16, null=True, blank=True)

	def __str__(self):
		return self.user.username + '\'s profile'

class Feature(models.Model):
	''' features built by 3rd party developers '''
	name = models.CharField(max_length=32)
	picture = models.ImageField(upload_to='feature_pictures/', null=True, blank=True)
	community_type = models.CharField(max_length=32, choices=CommunityType.choices)
	description = models.TextField()

	# used to validate
	key = models.CharField(max_length=10, unique=True)

	payload = models.TextField()

	def get_random_key(self):
		''' generate a random key '''
		_key = User.objects.make_random_password(length=10, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

		# check if the key already exists in another community and generate another
		if Feature.objects.filter(key=_key).exists():
			return self.get_random_key()

		return _key

	def save(self, *args, **kwargs):
		''' override the default save function '''

		# check if the object is being created
		if not self.id:
			# assign the key
			self.key = self.get_random_key()

		# call the parent save
		super(Feature, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Community(models.Model):
	''' communities which organisations create '''
	name = models.CharField(max_length=32)
	type = models.CharField(max_length=32, choices=CommunityType.choices)
	picture = models.ImageField(upload_to='community_pictures/', null=True, blank=True)
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
		''' generate a random key '''
		_key = User.objects.make_random_password(length=10, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")

		# check if the key already exists in another community and generate another
		if Community.objects.filter(key=_key).exists():
			return self.get_random_key()

		return _key

	def save(self, *args, **kwargs):
		''' override the default save function '''

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

# datastore models

class SimpleStore(models.Model):
	''' simple data store for features '''
	feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='simple_store')

	key = models.CharField(max_length=128)
	value = models.TextField()

	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='simple_store')
	community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='simple_store')

	access = models.CharField(max_length=32, choices=DataAccessType.choices)

	def __str__(self):
		return self.feature.name + '\'s simple store'

# class ListStore(models.Model):
# 	''' list data store for features '''
# 	feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='list_store')
#
# 	# should be unique for each list
# 	key = models.CharField(max_length=128)
# 	# member = models.ForeignKey(SimpleStore, on_delete=models.CASCADE, related_name='parent_list')
#
# 	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
# 	object_id = models.PositiveIntegerField(null=True, blank=True)
# 	member = GenericForeignKey('content_type', 'object_id')
#
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='list_store')
# 	community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='list_store')
#
# 	access = models.CharField(max_length=32, choices=DataAccessType.choices)
#
# 	def __str__(self):
# 		return self.feature.name + '\'s list store'
#
# class MapStore(models.Model):
# 	''' simple data store for features '''
# 	feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='map_store')
#
# 	# should be unique for each map
# 	key = models.CharField(max_length=128)
# 	# member = models.models.ForeignKey(SimpleStore, on_delete=models.CASCADE, related_name='parent_map')
#
# 	content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
# 	object_id = models.PositiveIntegerField(null=True, blank=True)
# 	member = GenericForeignKey('content_type', 'object_id')
#
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='map_store')
# 	community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='map_store')
#
# 	access = models.CharField(max_length=32, choices=DataAccessType.choices)
#
# 	def __str__(self):
# 		return self.feature.name + '\'s map store'
