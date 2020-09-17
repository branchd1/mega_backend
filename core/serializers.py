"""
This module contains Serializer classes for models.
These classes determine how model object should be serialized.

"""

from rest_framework import serializers

from core.models import Community, Feature, SimpleStore, CommunityType


# Serializers

class FeatureSerializer(serializers.ModelSerializer):
    """ Serialize Feature model """
    class Meta:
        model = Feature
        fields = '__all__'
        read_only_fields = ['id']


class CommunitySerializer(serializers.ModelSerializer):
    """ Serialize Community model """
    is_admin = serializers.BooleanField(read_only=True)
    type_value = serializers.CharField(source='get_community_type_value', read_only=True)

    class Meta:
        model = Community
        read_only_fields = ['id', 'key']
        exclude = ['admins', 'features', 'members']


class SimpleStoreSerializer(serializers.ModelSerializer):
    """ Serialize SimpleStore model """
    class Meta:
        model = SimpleStore
        fields = ['id', 'key', 'value']
        read_only_fields = ['id']


class CommunityTypeSerializer(serializers.ModelSerializer):
    """ Serialize CommunityType model """
    class Meta:
        model = CommunityType
        fields = '__all__'
        read_only_fields = ['id']