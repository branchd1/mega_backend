from django.shortcuts import render

from rest_framework import viewsets

from .models import Profile, Feature, Database, Community

from .serializers import ProfileSerializer, FeatureSerializer, DatabaseSerializer, CommunitySerializer

# Views here

class ProfileViewSet(viewsets.ModelViewSet):
	''' profile view set '''
	serializer_class = ProfileSerializer
	permission_classes = []
	
	def get_queryset(self):
		return self.request.user.profile.all()
		
class FeatureViewSet(viewsets.ModelViewSet):
	''' feature view set '''
	serializer_class = FeatureSerializer
	permission_classes = []
		
class DatabaseViewSet(viewsets.ModelViewSet):
	''' database view set '''
	serializer_class = DatabaseSerializer
	permission_classes = []
		
class CommunityViewSet(viewsets.ModelViewSet):
	''' community view set '''
	serializer_class = CommunitySerializer
	permission_classes = []
	