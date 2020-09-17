from django.test import TestCase
from developer.views import index, feature_details, \
    add_feature, edit_feature
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

# Test here


class DeveloperWebTest(TestCase):
    """ Test the developer website """
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test', password='test$$$')
        self.client = Client()
        self.client.force_login(self.user)

    def test_index_page_loads(self):
        _response = self.client.get(reverse('developer:index'))
        self.assertEqual(_response.status_code, 200)



