from django.forms import model_to_dict
from django.test import TestCase
from django.test.client import MULTIPART_CONTENT

from developer.views import index, feature_details, \
    add_feature, edit_feature
from developer.forms import FeatureForm
from core.models import Feature
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from django.conf import settings


# Test here


class DeveloperWebTest(TestCase):
    """ Test the developers website """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', password='test$$$')
        self.user_2 = User.objects.create_user(username='test2', password='test$$$')

        self.test_feature = Feature.objects.create(name='test', description='test',
                                                   picture=settings.BASE_DIR + settings.MEDIA_URL + 'dummy.png',
                                                   payload='test', user=self.user)
        self.test_feature_2 = Feature.objects.create(name='test2', description='test2',
                                                     picture=settings.BASE_DIR + settings.MEDIA_URL + 'dummy.png',
                                                     payload='test2', user=self.user_2)

        self.client = Client()
        self.client.force_login(self.user)

    def test_index_page_loads(self):
        """ Test that the index page loads """
        _response = self.client.get(reverse('developer:index'))
        self.assertEqual(_response.status_code, 200)

    def test_feature_detail_page_loads(self):
        """ Test that the feature detail page loads """
        _response = self.client.get(reverse('developer:feature_details', kwargs={'feature_id': self.test_feature.pk}))
        self.assertEqual(_response.status_code, 200)

    def test_edit_feature_page_loads(self):
        """ Test that the edit feature page loads """
        _response = self.client.get(reverse('developer:edit_feature', kwargs={'feature_id': self.test_feature.pk}))
        self.assertEqual(_response.status_code, 200)

    def test_add_feature_page_loads(self):
        """ Test that the add feature page loads """
        _response = self.client.get(reverse('developer:add_feature'))
        self.assertEqual(_response.status_code, 200)

    def test_accurate_feature_details_are_displayed(self):
        """ Test that the correct feature details are displayed on the page """
        _response = self.client.get(reverse('developer:feature_details', kwargs={'feature_id': self.test_feature.pk}))
        self.assertEqual(self.test_feature, _response.context['feature'])

    def test_accurate_features_are_displayed(self):
        """ Test that the correct features are displayed on the page """
        _response = self.client.get(reverse('developer:index'))
        self.assertIn(self.test_feature, _response.context['features'])
        self.assertNotIn(self.test_feature_2, _response.context['features'])

    def test_feature_is_created(self):
        """ Test that the feature is created """
        _name = 'unique_test_2222'
        _response = self.client.post(reverse('developer:add_feature'), data={
            'name': _name,
            'description': 'test',
            'picture': open(settings.BASE_DIR + settings.MEDIA_URL + 'dummy.png', 'rb'),
            'payload': 'test'
        })

        # assert that the feature with that unique name was created now
        self.assertTrue(Feature.objects.filter(name=_name).exists())

    def test_feature_is_edited(self):
        """ Test that the feature is edited """
        _name = 'edited_name'
        _dict = model_to_dict(self.test_feature)
        # change name
        _dict['name'] = _name
        _dict['approved'] = True
        _response = self.client.post(reverse('developer:edit_feature', kwargs={'feature_id': self.test_feature.pk}),
                                     data=_dict)

        # assert that the name was changed to the edited name
        self.assertTrue(Feature.objects.filter(name=_name).exists())
