from django.shortcuts import render
from rest_framework import viewsets, views

from rest_framework.response import Response

from core import serializers as my_serializers

from core.permissions import IsOwner

from core.models import Community, Feature, DataAccessType, SimpleStore, UploadedImage

from django.contrib.auth.models import User

from django.db.models import Q, BooleanField, Value

from itertools import chain

from rest_framework.parsers import FileUploadParser

from django.core.files.base import ContentFile

import io

from django.core.files.images import ImageFile


# Views here

class ProfileViewSet(viewsets.ModelViewSet):
    """ profile view set """
    serializer_class = my_serializers.ProfileSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        """ return the current user profile only """
        return self.request.user.profile.all()


class FeatureViewSet(viewsets.ModelViewSet):
    """ feature view set """
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
    """ simple store view set """
    serializer_class = my_serializers.SimpleStoreSerializer
    permission_classes = []


# class ListStoreViewSet(viewsets.ModelViewSet):
# 	""" list store view set """
# 	serializer_class = my_serializers.ListStoreSerializer
# 	permission_classes = []
#
# class MapStoreViewSet(viewsets.ModelViewSet):
# 	""" map store view set """
# 	serializer_class = my_serializers.MapStoreSerializer
# 	permission_classes = []

class CommunityViewSet(viewsets.ModelViewSet):
    """ community view set """
    serializer_class = my_serializers.CommunitySerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        community = serializer.save()
        community.admins.add(self.request.user)

    def get_queryset(self):
        """ return current user communities only """
        _user = self.request.user
        _queryset1 = Community.objects.filter(admins__id__contains=_user.pk).distinct().annotate(
            is_admin=Value(True, output_field=BooleanField()))
        _queryset2 = Community.objects.filter(members__id__contains=_user.pk).distinct().annotate(
            is_admin=Value(False, output_field=BooleanField()))

        _queryset = list(chain(_queryset1, _queryset2))

        return _queryset


class CheckEmail(views.APIView):
    """ checks if an email exists """

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
    """ checks if an email exists """

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
    """ add a feature to a community """

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
    """ stores data sent """

    def get(self, request):
        _tag = request.GET.get('mega$tag')

        _community_id = request.GET.get('mega$community')
        _community = Community.objects.get(pk=_community_id)

        _feature_key = request.GET.get('mega$feature')
        _feature = Feature.objects.get(key=_feature_key)

        _stores = SimpleStore.objects.filter(feature=_feature, key=_tag, community=_community)

        _filter_stores_id_by_access = []
        for _store in _stores:
            if filter_stores_by_access(_store, request.user) is not None:
                _filter_stores_id_by_access.append(_store.pk)

        _stores = _stores.filter(id__in=_filter_stores_id_by_access)

        _res = my_serializers.SimpleStoreSerializer(_stores, many=True)

        _res_data = _res.data

        return Response(_res_data)

    def post(self, request):
        _data = request.data

        _tag = request.data.get('mega$tag')

        _access = None
        _access_proxy = request.data.get('mega$access')
        if _access_proxy == 'public':
            _access = DataAccessType.COMMUNITY
        elif _access_proxy == 'admin':
            _access = DataAccessType.ADMIN
        else:
            _access = DataAccessType.USER

        _community_id = request.data.get('mega$community')
        _community = Community.objects.get(pk=_community_id)

        _feature_key = request.data.get('mega$feature')
        _feature = Feature.objects.get(key=_feature_key)

        # remove special keys
        _special_keys = []

        for key, val in _data.items():
            if 'mega$' in key:
                _special_keys.append(key)

        for key in _special_keys:
            del _data[key]

        # create map store
        store = SimpleStore.objects.create(feature=_feature, key=_tag, access=_access, user=request.user,
                                           community=_community, value=_data)

        return Response({}, status=201)


class UploadImage(views.APIView):
    """ upload image and return URL """
    parser_class = (FileUploadParser,)

    def post(self, request):
        image = ImageFile(io.BytesIO(request.body))
        uploaded_image = UploadedImage.objects.create(image=image)
        return Response({'url': uploaded_image.image.url})


# helper functions
def filter_stores_by_access(store, user):
    if store.access == DataAccessType.USER:
        if store.user == user:
            return store
        return None
    elif store.access == DataAccessType.COMMUNITY:
        if store.is_admin_or_member(user):
            return store
        return None
    elif store.access == DataAccessType.ADMIN:
        if store.is_admin(user):
            return store
        return None
