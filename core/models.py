from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

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
	
	payload = models.TextField()
	
	def __str__(self):
		return self.name
		
class Database(models.Model):
	''' database connection information used by features '''
	feature = models.OneToOneField(Feature, on_delete=models.CASCADE, related_name='database')
	
	db_name = models.CharField(max_length=32)
	db_pass = models.CharField(max_length=32)
	db_host = models.CharField(max_length=32)
	db_port = models.IntegerField()
	
	def __str__(self):
		return self.feature.name + '\'s database'
	

class Community(models.Model):
	''' communities which organisations create '''
	name = models.CharField(max_length=32)
	type = models.CharField(max_length=32, choices=CommunityType.choices)
	picture = models.ImageField(upload_to='community_pictures/', null=True, blank=True)
	description = models.TextField()
	
	# determines if the community can be joined by anyone or only by people with the key
	is_public = models.BooleanField()
	
	# used to join the community if it is not public
	key = models.CharField(max_length=16)
	
	# django automatically creates the relationship model for many-to-many fields
	admins = models.ManyToManyField(User, related_name='communities_admined', blank=True)
	members = models.ManyToManyField(User, related_name='communities_joined', blank=True)
	
	features = models.ManyToManyField(Feature, related_name='communities_using', blank=True)
	
	class Meta:
		verbose_name_plural = 'communities'
		ordering = ['id']
		
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
		
