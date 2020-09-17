""" This module contains the core views in the backend """

from rest_framework import viewsets, views

from rest_framework.response import Response

from core import serializers as my_serializers

from core.permissions import IsOwner

from core.models import Community, Feature, DataAccessType, SimpleStore, UploadedImage, CommunityType

from django.contrib.auth.models import User

from django.db.models import BooleanField, Value

from itertools import chain

from rest_framework.parsers import MultiPartParser

from django.contrib.sites.models import Site


# Helper functions

def filter_stores_by_access(store, user):
    """
    Check if the current user has the appropriate permission to access the store

    Parameters
    ----------
    store : SimpleStore
        The store object
    user : User
        The user who sent the request

    Returns
    -------
    object
        The store object if the user has the permission, None otherwise

    """
    if store.access == DataAccessType.USER:
        if store.user == user:
            return store
        return None
    elif store.access == DataAccessType.COMMUNITY:
        if store.is_admin_or_member(user):
            return store
        return None
    elif store.access == DataAccessType.ADMIN:
        if store.is_admin(user) or store.user == user:
            return store
        return None


# Views

class FeatureViewSet(viewsets.ModelViewSet):
    """Feature view set

    Contains API views to perform CRUD operation on Features

    """
    serializer_class = my_serializers.FeatureSerializer

    def get_queryset(self):
        # get user
        _user = self.request.user

        # get the community id from GET params
        _community_id = self.request.GET.get('community')

        # check if all features are being queried for
        _all_features = self.request.GET.get('all')

        if _all_features:
            # if all features are being queried for,
            try:
                _community = Community.objects.get(id=_community_id)
            except Community.DoesNotExist:
                _queryset = Feature.objects.filter(approved=True)
                return _queryset
            used_features_id = _community.features.all().values('id')

            # return all approved features excluding features that have been used in this community
            _queryset = Feature.objects.filter(approved=True).exclude(id__in=used_features_id)
            return _queryset

        if _community_id:
            # if there is a community id
            try:
                _community = Community.objects.get(id=_community_id)
            except Community.DoesNotExist:
                return None
            if not _community.is_admin_or_member(_user):
                return None

            # return features that are in the community and approved
            _queryset = _community.features.filter(approved=True)
            return _queryset

        return None


class CommunityTypeViewSet(viewsets.ModelViewSet):
    """CommunityType view set

    Contains API views to perform CRUD operation on Community types

    """
    serializer_class = my_serializers.CommunityTypeSerializer
    queryset = CommunityType.objects.all()


class CommunityViewSet(viewsets.ModelViewSet):
    """Community view set

    Contains API views to perform CRUD operation on Communities

    """
    serializer_class = my_serializers.CommunitySerializer
    permission_classes = [IsOwner]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        # get the object representing the community type
        _community_type = CommunityType.objects.get(value=serializer.validated_data['type'])
        community = serializer.save()

        # add the creator to the list of admins
        community.admins.add(self.request.user)

    def get_queryset(self):
        # return the current user communities only
        _user = self.request.user

        # add "is_admin" field to result,
        # so that the frontend can know which communities the user is an admin or just a member
        _queryset1 = Community.objects.filter(admins__id__contains=_user.pk).distinct().annotate(
            is_admin=Value(True, output_field=BooleanField()))
        _queryset2 = Community.objects.filter(members__id__contains=_user.pk).distinct().annotate(
            is_admin=Value(False, output_field=BooleanField()))

        # join queryset of communities where current user is admin and member together
        _queryset = list(chain(_queryset1, _queryset2))

        return _queryset


class CheckEmail(views.APIView):
    """Check Email View

    Checks if an email exists

    """

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
    """Join Community View

    Join a community

    """

    def post(self, request):
        _key = request.data.get('key')
        if _key:
            _response_dict = None
            try:
                _community = Community.objects.get(key=_key)
            except Community.DoesNotExist:
                # community does not exist
                _response_dict = {
                    'key': 'Incorrect key'
                }
                return Response(_response_dict, status=400)

            # add user to community members, if not already a member
            if request.user not in _community.members.all():
                _community.members.add(request.user)

            return Response({})
        else:
            _response_dict = {
                'key': 'Enter a key'
            }
            return Response(_response_dict, status=400)


class LeaveCommunity(views.APIView):
    """ Leave a community """

    def post(self, request):
        _community_pk = request.data.get('community')
        if _community_pk:
            # if there was a community
            _response_dict = None
            try:
                _community = Community.objects.get(pk=_community_pk)
            except Community.DoesNotExist:
                _response_dict = {
                    'community': 'Community does not exist'
                }
                return Response(_response_dict, status=400)
            # check user is in community then remove
            if request.user in _community.members.all():
                _community.members.remove(request.user)
            return Response({})
        else:
            # if there wasn't a community
            _response_dict = {
                'community': 'Enter a community'
            }
            return Response(_response_dict, status=400)


class RemoveFeature(views.APIView):
    """ Remove a feature from community """

    def post(self, request):
        _community_pk = request.data.get('community')
        _feature_pk = request.data.get('feature')
        if _community_pk and _feature_pk:
            _response_dict = None

            try:
                _community = Community.objects.get(pk=_community_pk)
            except Community.DoesNotExist:
                _response_dict = {
                    'community': 'Community does not exist'
                }
                return Response(_response_dict, status=400)

            try:
                _feature = Feature.objects.get(pk=_feature_pk)
            except Feature.DoesNotExist:
                _response_dict = {
                    'feature': 'Feature does not exist'
                }
                return Response(_response_dict, status=400)

            # check user is admin before removing
            if _community.is_admin(request.user):
                _community.features.remove(_feature)

            return Response({})
        elif _community_pk is None:
            _response_dict = {
                'community': 'Enter a community'
            }
            return Response(_response_dict, status=400)
        else:
            _response_dict = {
                'feature': 'Enter a feature'
            }
            return Response(_response_dict, status=400)


class AddFeatureToCommunity(views.APIView):
    """ Add a feature to a community """

    def post(self, request):
        _community_id = request.data.get('community')
        _feature_id = request.data.get('feature')

        if not _community_id:
            _response_dict = {
                'community': 'Enter a community'
            }
            return Response(_response_dict, status=400)

        if not _feature_id:
            _response_dict = {
                'feature': 'Enter a feature'
            }
            return Response(_response_dict, status=400)

        try:
            _community = Community.objects.get(id=_community_id)
        except Community.DoesNotExist:
            _response_dict = {
                'community': 'Community does not exist'
            }
            return Response(_response_dict, status=400)

        try:
            _feature = Feature.objects.get(id=_feature_id)
        except Feature.DoesNotExist:
            _response_dict = {
                'feature': 'Feature does not exist'
            }
            return Response(_response_dict, status=400)

        _community.features.add(_feature)

        return Response({})


class DataStore(views.APIView):
    """ Data Store API views """

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

    def delete(self, request, store_id):
        _no_access_response_dict = {
            'access': 'User does not have access to delete'
        }

        try:
            _store = SimpleStore.objects.get(id=store_id)
        except SimpleStore.DoesNotExist:
            _response_dict = {
                'datastore': 'Store data does not exist'
            }
            return Response(_response_dict, status=400)

        if _store.access == DataAccessType.USER and not _store.user == request.user:
            return Response(_no_access_response_dict, status=403)

        if _store.access == DataAccessType.COMMUNITY and not _store.community.is_admin_or_member(_store.user):
            return Response(_no_access_response_dict, status=403)

        if _store.access == DataAccessType.ADMIN and not _store.community.is_admin(_store.user):
            return Response(_no_access_response_dict, status=403)

        _store.delete()

        return Response({})


class UploadImage(views.APIView):
    """ upload image and return URL """
    parser_class = (MultiPartParser,)

    def post(self, request):
        uploaded_image = UploadedImage.objects.create(image=request.FILES['file'])

        current_site = Site.objects.get_current()

        # remove hardcoded 'http://'
        return Response({'url': 'http://' + current_site.domain + uploaded_image.image.url})
