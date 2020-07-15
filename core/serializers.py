from rest_framework import serializers

from . import models as my_models

from django.contrib.auth.models import User

# Serializers

class UserSerializer(serializers.ModelSerializer):
	''' Serializer users '''
	class Meta:
		model = User
		fields = '__all__'
		write_only_fields = ['password']
	
	def create(self, validated_data):
		user = User.objects.create(
			username=validated_data['username'],
			email=validated_data['email'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
		)
        
		# used to make sure password is stored as a hash
		user.set_password(validated_data['password'])
		user.save()

		return user

class ProfileSerializer(serializers.ModelSerializer):
	''' Serialize profile '''
	class Meta:
		model = my_models.Profile
		fields = '__all__'
		read_only_fields = ['id']
		
class FeatureSerializer(serializers.ModelSerializer):
	''' Serialize feature '''
	class Meta:
		model = my_models.Feature
		fields = '__all__'
		read_only_fields = ['id']
		
class DatabaseSerializer(serializers.ModelSerializer):
	''' Serialize database '''
	class Meta:
		model = my_models.Database
		fields = '__all__'
		read_only_fields = ['id']
		
class CommunitySerializer(serializers.ModelSerializer):
	''' Serialize community '''
	class Meta:
		model = my_models.Community
		fields = '__all__'
		read_only_fields = ['id']