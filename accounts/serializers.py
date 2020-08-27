from rest_framework import serializers

from django.contrib.auth.models import User

from accounts.models import Profile


class SpecialUserSerializer(serializers.ModelSerializer):
    """ Serialize user """

    class Meta:
        model = User
        read_only_fields = ['id']
        exclude = ['username']


class ProfileSerializer(serializers.ModelSerializer):
    """ Serialize profile """

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id']
