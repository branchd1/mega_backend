from rest_framework import serializers

from .models import Profile, Feature, Database, Community

# Serializers

class ProfileSerializer(serializers.Serializer):
	''' Serialize profile '''
	class Meta:
		model = Profile
		fields = '__all__'
		read_only_fields = ['id']
		
class FeatureSerializer(serializers.Serializer):
	''' Serialize feature '''
	class Meta:
		model = Feature
		fields = '__all__'
		read_only_fields = ['id']
		
class DatabaseSerializer(serializers.Serializer):
	''' Serialize database '''
	class Meta:
		model = Database
		fields = '__all__'
		read_only_fields = ['id']
		
class CommunitySerializer(serializers.Serializer):
	''' Serialize community '''
	class Meta:
		model = Community
		fields = '__all__'
		read_only_fields = ['id']