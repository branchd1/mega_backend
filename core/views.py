from django.shortcuts import render

from rest_framework import viewsets, views

from rest_framework.response import Response

from core import serializers as my_serializers

from core.permissions import IsOwner

from core.models import Community, Feature

from django.contrib.auth.models import User

from django.db.models import Q, BooleanField, Value

from itertools import chain

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

	def get_queryset(self):
		_user = self.request.user
		_community_id = self.request.GET.get('community')
		_community_type = self.request.GET.get('type')
		if _community_type:
			try:
				_community = Community.objects.get(id=_community_id)
			except Community.DoesNotExist:
				return None
			used_features_id = _community.features.all().values('id')
			_queryset = Feature.objects.filter(community_type=_community_type).exclude(id__in=used_features_id)
			return _queryset
		if _community_id:
			try:
				_community = Community.objects.get(id=_community_id)
			except Community.DoesNotExist:
				return None
			if not _community.is_admin_or_member(_user):
				return None
			_queryset = _community.features.all()
			return _queryset
		return None

class SimpleStoreViewSet(viewsets.ModelViewSet):
	''' simple store view set '''
	serializer_class = my_serializers.SimpleStoreSerializer
	permission_classes = []

class ListStoreViewSet(viewsets.ModelViewSet):
	''' list store view set '''
	serializer_class = my_serializers.ListStoreSerializer
	permission_classes = []

class MapStoreViewSet(viewsets.ModelViewSet):
	''' map store view set '''
	serializer_class = my_serializers.MapStoreSerializer
	permission_classes = []

class CommunityViewSet(viewsets.ModelViewSet):
	''' community view set '''
	serializer_class = my_serializers.CommunitySerializer
	permission_classes = [IsOwner]

	def perform_create(self, serializer):
		community = serializer.save()
		community.admins.add(self.request.user)

	def get_queryset(self):
		''' return current user communities only '''
		_user = self.request.user
		_queryset1 = Community.objects.filter(admins__id__contains=_user.pk).distinct().annotate(is_admin=Value(True, output_field=BooleanField()))
		_queryset2 = Community.objects.filter(members__id__contains=_user.pk).distinct().annotate(is_admin=Value(False, output_field=BooleanField()))

		_queryset = list(chain(_queryset1, _queryset2))

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

class JoinCommunity(views.APIView):
	''' checks if an email exists '''
	def post(self, request):
		_key = request.data.get('key')
		if _key:
			_response_dict = None
			try:
				_community = Community.objects.get(key=_key)
			except Community.DoesNotExist:
				# email has not been used
				_response_dict = {
					'key': 'Incorrect key'
				}
				return Response(_response_dict, status=400)
			# email has been used
			_community.members.add(request.user)
			return Response({})
		else:
			_response_dict = {
				'key': 'Enter a key'
			}
			return Response(_response_dict, status=400)

class AddFeatureToCommunity(views.APIView):
	''' add a feature to a community '''
	def post(self, request):
		_community_id = request.data.get('community')
		_feature_id = request.data.get('feature')

		if not _community_id:
			_response_dict = {
				'community': 'Pick a community'
			}
			return Response(_response_dict, status=400)

		if not _feature_id:
			_response_dict = {
				'feature': 'Pick a feature'
			}
			return Response(_response_dict, status=400)

		try:
			_feature = Feature.objects.get(id=_feature_id)
		except Feature.DoesNotExist:
			_response_dict = {
				'feature': 'Invalid feature'
			}
			return Response(_response_dict, status=400)

		try:
			_community = Community.objects.get(id=_community_id)
		except Feature.DoesNotExist:
			_response_dict = {
				'community': 'Invalid community'
			}
			return Response(_response_dict, status=400)

		_community.features.add(_feature)

		return Response({})

class DataStore(views.APIView):
	''' stores data sent '''
	def get(self, request):
		pass
		# _key = request.data.get('key')
		# if _key:
		# 	_response_dict = None
		# 	try:
		# 		_community = Community.objects.get(key=_key)
		# 	except Community.DoesNotExist:
		# 		# email has not been used
		# 		_response_dict = {
		# 			'key': 'Incorrect key'
		# 		}
		# 		return Response(_response_dict, status=400)
		# 	# email has been used
		# 	_community.members.add(request.user)
		# 	return Response({})
		# else:
		# 	_response_dict = {
		# 		'key': 'Enter a key'
		# 	}
		# 	return Response(_response_dict, status=400)

	def post(self, request):
		_data = request.data
		print(_data)
		return Response({})
