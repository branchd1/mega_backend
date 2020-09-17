""" Tests for accounts related logic """

from django.test import TestCase
from django.urls import reverse
from djoser.conf import User
from rest_framework.test import APIRequestFactory, force_authenticate

from accounts.models import Profile
from accounts.views import ProfileViewSet

# Test here


class ProfileViewTest(TestCase):
    """ Test ProfileViewSet """
    def setUp(self) -> None:
        # profile automatically created
        self.user = User.objects.create_user(username='test', password='test1$$$$')

    def test_profile_queryset_correct(self):
        """ Check that profile queryset returns only users profile """
        factory = APIRequestFactory()

        request = factory.get(reverse('profile-list'))
        force_authenticate(request, user=self.user)
        view = ProfileViewSet.as_view(actions={'get': 'list'})
        _response = view(request)
        # check only one profile returned and check it is the correct profile
        self.assertEqual(len(_response.data), 1)
        self.assertEqual(_response.data[0]['id'], self.user.profile.pk)


class SignalsTest(TestCase):
    """ Test signals firing properly """
    def setUp(self) -> None:
        self._email = 'test@test.com'

        # profile automatically created - test
        self.user = User.objects.create_user(username='test', password='test1$$$$')

        self.user_2 = User(email=self._email, password='test1$$$$')
        self.user_2.save()

    def test_profile_created(self):
        """ Check that profile was created when user was created """
        self.assertTrue(self.user.profile is not None)

    def test_username_is_assigned_when_user_created(self):
        """ Check that username is given to a user when user is registered """
        self.assertEqual(self.user_2.username, self._email)
        self.assertTrue(self.user_2.username is not None)

