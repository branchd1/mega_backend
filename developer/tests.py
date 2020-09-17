from django.test import TestCase
from developer.views import index, feature_details, \
    add_feature, edit_feature
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

# Test here


class DeveloperWebTest(TestCase):
    """ Test the developer website """
    

