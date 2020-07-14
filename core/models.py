from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

# Constants
class CommunityType(models.TextChoices):
	''' specifies the types of communities '''
	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')
# 	BAR = 'BAR', _('Bar')

# Create your models here.
class Profile(models.Model):
	''' user profile to hold extra data from django's default User class '''
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
	phone_number = models.CharField(max_length=16, null=True, blank=True)
	
	def __str__(self):
		return self.user.username + _('\'s profile')
	
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
		return self.feature.name + _('\'s database')
	

class Community(models.Model):
	''' communities which organisations create '''
	name = models.CharField(max_length=32)
	type = models.CharField(max_length=32, choices=CommunityType.choices)
	picture = models.ImageField(upload_to='community_pictures/', null=True, blank=True)
	description = models.TextField()
	
	is_public = models.BooleanField()
	key = models.CharField(max_length=16)
	
	admins = models.ManyToManyField(User, related_name='communities_admined')
	members = models.ManyToManyField(User, related_name='communities_joined')
	
	features = models.ManyToManyField(Feature)
	
	def __str__(self):
		return self.name