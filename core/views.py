from django.shortcuts import render

from rest_framework import viewsets

from . import serializers as my_serializers

from .permissions import IsOwner

# Views here

class ProfileViewSet(viewsets.ModelViewSet):
	''' profile view set '''
	serializer_class = my_serializers.ProfileSerializer
	permission_classes = [IsOwner]
	
	def get_queryset(self):
		''' return the current user profile only '''
		return self.request.user.profile.all()
		
class FeatureViewSet(viewsets.ModelViewSet):
	''' feature view set '''
	serializer_class = my_serializers.FeatureSerializer
	permission_classes = []
		
class DatabaseViewSet(viewsets.ModelViewSet):
	''' database view set '''
	serializer_class = my_serializers.DatabaseSerializer
	permission_classes = []
		
class CommunityViewSet(viewsets.ModelViewSet):
	''' community view set '''
	serializer_class = my_serializers.CommunitySerializer
	permission_classes = []
	