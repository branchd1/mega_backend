from django.shortcuts import render

from rest_framework import viewsets, views

from rest_framework.response import Response

from core import serializers as my_serializers

from core.permissions import IsOwner

from core.models import Community

from django.contrib.auth.models import User

from django.http import JsonResponse

from django.db.models import Q

from django.db.models import BooleanField, Value

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
	permission_classes = [IsOwner]
	
	def get_queryset(self):
		''' return current user communities only '''
		_user = self.request.user
		_queryset1 = Community.objects.filter(admins__id__contains=_user.pk).distinct().annotate(is_admin=Value(True, output_field=BooleanField()))
		_queryset2 = Community.objects.filter(members__id__contains=_user.pk).distinct().annotate(is_admin=Value(False, output_field=BooleanField()))
		_queryset = _queryset1 | _queryset2
		return _queryset
	
class CheckEmail(views.APIView):
	''' checks if an email exists '''
	def post(self, request):
		email = request.data.get('email')
		if email:
			_response_dict = None
			if User.objects.filter(email=email).exists():
				# email has been used
				_response_dict = {
					'exists': True
				}
			else:
				# email has not been used
				_response_dict = {
					'exists': False
				}
			return Response(_response_dict)
		else:
			_response_dict = {
				'email': 'Enter an email address'
			}
			return Response(_response_dict, status=400)
			
	