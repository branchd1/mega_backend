from django.shortcuts import render

from rest_framework import viewsets

from core import serializers as my_serializers

from core.permissions import IsOwner

from django.contrib.auth.models import User

from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

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
	
@csrf_exempt
def check_email(request):
	''' checks if an email exists '''
	email = request.POST.get('email')
	print(request.POST)
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
		return JsonResponse(_response_dict)
	else:
		_response_dict = {
			'email': 'Enter an email address'
		}
		return JsonResponse(_response_dict, status=400)
			
	