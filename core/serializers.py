from rest_framework import serializers

from . import models as my_models


# Serializers

class FeatureSerializer(serializers.ModelSerializer):
    """ Serialize feature """
    class Meta:
        model = my_models.Feature
        fields = '__all__'
        read_only_fields = ['id']


class CommunitySerializer(serializers.ModelSerializer):
    """ Serialize community """
    is_admin = serializers.BooleanField(read_only=True)

    class Meta:
        model = my_models.Community
        read_only_fields = ['id', 'key']
        exclude = ['admins', 'features', 'members']


class SimpleStoreSerializer(serializers.ModelSerializer):
    """ Serialize simple store """
    class Meta:
        model = my_models.SimpleStore
        fields = ['id', 'key', 'value']
        read_only_fields = ['id']