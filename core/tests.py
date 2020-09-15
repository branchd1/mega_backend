from django.test import TestCase
from core.models import Feature, CommunityType, Community, SimpleStore, UploadedImage
from django.contrib.auth.models import User
from django.test.client import Client


# Create your tests here.
class FeatureTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.testFeature = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature1 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature2 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature3 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature4 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)

    def test_feature_key_unique(self):
        self.assertNotEqual(self.testFeature.key, self.testFeature1.key)
