from django.test import TestCase
from core.models import Feature, CommunityType, Community, SimpleStore, UploadedImage
from django.contrib.auth.models import User
from django.test.client import Client


# Create your tests here.
class FeatureModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.testFeature = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature1 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature2 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature3 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.testFeature4 = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)

    def test_feature_key_is_unique(self):
        """ Check that feature keys are always unique """
        self.assertNotEqual(self.testFeature.key, self.testFeature1.key)
        self.assertNotEqual(self.testFeature.key, self.testFeature2.key)
        self.assertNotEqual(self.testFeature.key, self.testFeature3.key)
        self.assertNotEqual(self.testFeature.key, self.testFeature4.key)
