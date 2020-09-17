from django.test import TestCase
from core.models import Feature, CommunityType, Community
from core.views import FeatureViewSet, CommunityViewSet, \
    CheckEmail, JoinCommunity, LeaveCommunity, RemoveFeature, \
    AddFeatureToCommunity
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.urls import reverse


# Tests here

class FeatureModelTestCase(TestCase):
    """ Test Feature Model """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.test_feature = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
        self.test_feature_1 = Feature.objects.create(name='test', description='', picture='', payload='',
                                                     user=self.user)
        self.test_feature_2 = Feature.objects.create(name='test', description='', picture='', payload='',
                                                     user=self.user)
        self.test_feature_3 = Feature.objects.create(name='test', description='', picture='', payload='',
                                                     user=self.user)
        self.test_feature_4 = Feature.objects.create(name='test', description='', picture='', payload='',
                                                     user=self.user)

    def test_feature_key_is_unique(self) -> None:
        """ Check that feature keys are always unique """
        self.assertNotEqual(self.test_feature.key, self.test_feature_1.key)
        self.assertNotEqual(self.test_feature.key, self.test_feature_2.key)
        self.assertNotEqual(self.test_feature.key, self.test_feature_3.key)
        self.assertNotEqual(self.test_feature.key, self.test_feature_4.key)


class CommunityModelTestCase(TestCase):
    """ Test Community Model """

    def setUp(self) -> None:
        self.admin_user = User.objects.create_user(username='alice', password="alice2$$$")
        self.member_user = User.objects.create_user(username='alice2', password="alice2$$$")
        self.non_member_user = User.objects.create_user(username='alice3', password="alice2$$$")
        self.non_member_user_1 = User.objects.create_user(username='alice4', password="alice2$$$")

        self.restaurant_type = CommunityType.objects.create(value='restaurant')

        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')
        self.test_community_1 = Community.objects.create(name='test1', type=self.restaurant_type,
                                                         picture='', description='')
        self.test_community_2 = Community.objects.create(name='test2', type=self.restaurant_type,
                                                         picture='', description='')
        self.test_community_3 = Community.objects.create(name='test3', type=self.restaurant_type,
                                                         picture='', description='')
        self.test_community_4 = Community.objects.create(name='test4', type=self.restaurant_type,
                                                         picture='', description='')

        self.test_community.admins.add(self.admin_user)
        self.test_community.members.add(self.member_user)

    def test_community_key_is_unique(self) -> None:
        """ Check that community key is always unique """
        self.assertNotEqual(self.test_community.key, self.test_community_1.key)
        self.assertNotEqual(self.test_community.key, self.test_community_2.key)
        self.assertNotEqual(self.test_community.key, self.test_community_3.key)
        self.assertNotEqual(self.test_community.key, self.test_community_4.key)

    def test_is_admin_or_member(self) -> None:
        """ Check that the is_admin_or_member function accurately detects whether a user is an admin or member """
        self.assertTrue(self.test_community.is_admin_or_member(self.admin_user))
        self.assertTrue(self.test_community.is_admin_or_member(self.member_user))
        self.assertFalse(self.test_community.is_admin_or_member(self.non_member_user))
        self.assertFalse(self.test_community.is_admin_or_member(self.non_member_user_1))

    def test_is_admin(self) -> None:
        """ Check that the is_admin function accurately detects whether a user is an admin """
        self.assertTrue(self.test_community.is_admin(self.admin_user))
        self.assertFalse(self.test_community.is_admin(self.member_user))
        self.assertFalse(self.test_community.is_admin(self.non_member_user))
        self.assertFalse(self.test_community.is_admin(self.non_member_user_1))

    def test_get_community_type_value(self) -> None:
        """ Check that get_community_type_value function gets the accurate community type value """
        self.assertEqual(self.restaurant_type.value, self.test_community.get_community_type_value())
        self.assertEqual('restaurant', self.test_community.get_community_type_value())


class FeatureViewTestCase(TestCase):
    """ Test views related Feature """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.restaurant_type = CommunityType.objects.create(value='restaurant')
        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')
        self.test_feature = Feature.objects.create(name='test', description='',
                                                   picture='', payload='', user=self.user, approved=True)
        self.test_feature_2 = Feature.objects.create(name='test2', description='',
                                                     picture='', payload='', user=self.user, approved=True)

        self.test_community.features.add(self.test_feature)
        self.test_community.admins.add(self.user)

    def test_feature_queryset_is_accurate(self) -> None:
        """ Check that features returned by get_queryset method are the correct features """
        factory = APIRequestFactory()
        request = factory.get(reverse('core:check_email'), {'community': self.test_community.id}, format='json')

        view = FeatureViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        # assert nothing is returned in an unauthenticated request
        self.assertEqual(response.data, [])

        force_authenticate(request, user=self.user)
        response = view(request)
        # assert the accurate feature is returned in an authenticated request
        self.assertEqual(response.data[0]['id'], self.test_feature.id)

        request_2 = factory.get(reverse('core:check_email'), {'all': 'true'}, format='json')
        response_2 = view(request_2)
        # assert the accurate feature is when all features are requested
        self.assertEqual(response_2.data[0]['id'], self.test_feature.id)
        self.assertEqual(response_2.data[1]['id'], self.test_feature_2.id)

        request_3 = factory.get(reverse('core:check_email'), {'all': 'true', 'community': self.test_community.id}, format='json')
        response_3 = view(request_3)
        # assert the accurate feature is when all unused features are requested
        self.assertEqual(response_3.data[0]['id'], self.test_feature_2.id)


class CommunityViewTestCase(TestCase):
    """ Test views related Community """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.restaurant_type = CommunityType.objects.create(value='restaurant')
        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')
        self.test_community_2 = Community.objects.create(name='test2', type=self.restaurant_type,
                                                         picture='', description='')
        self.test_community_3 = Community.objects.create(name='test3', type=self.restaurant_type,
                                                         picture='', description='')
        self.test_community_4 = Community.objects.create(name='test4', type=self.restaurant_type,
                                                         picture='', description='')
        self.test_community.admins.add(self.user)
        self.test_community_2.members.add(self.user)

    def test_community_perform_create(self) -> None:
        """ Check that the CommunityViewSet perform_create function works accurately """
        factory = APIRequestFactory()
        request = factory.post(reverse('community-list'),
                               {'name': 'test',
                                'type': self.restaurant_type.id,
                                },
                               format='multipart'
                               )
        force_authenticate(request, user=self.user)
        view = CommunityViewSet.as_view(actions={'post': 'create'})
        response = view(request)

        community = Community.objects.get(pk=response.data['id'])

        # assert the user was added as a community admin
        self.assertIn(self.user, community.admins.all())

    def test_community_queryset_is_accurate(self):
        """ Check that communities returned by get_queryset method are correct """
        factory = APIRequestFactory()
        request = factory.get(reverse('community-list'))

        force_authenticate(request, user=self.user)
        view = CommunityViewSet.as_view(actions={'get': 'list'})
        response = view(request)
        # assert the appropriate community count are returned in response
        self.assertEqual(len(response.data), 2)

        # get ids of communities in response
        ids = list(map(lambda response_dict: response_dict['id'], response.data))

        # assert the appropriate communities are returned in response
        self.assertIn(self.test_community.id, ids)
        self.assertIn(self.test_community_2.id, ids)
        self.assertNotIn(self.test_community_3.id, ids)
        self.assertNotIn(self.test_community_4.id, ids)


class CheckEmailViewTestCase(TestCase):
    """ Test CheckEmail API view """

    def setUp(self) -> None:
        # there is a signal that automatically assigns email to username, so no need to specify
        self.user = User(email='alice@yahoo.com', password="alice2$$$")
        self.user.save()

    def test_check_email(self) -> None:
        """ Check that the view returns true if email exists in database and false otherwise """
        factory = APIRequestFactory()

        request = factory.post(reverse('core:check_email'), {'email': 'alice@yahoo.com'}, format='json')
        force_authenticate(request, user=self.user)
        view = CheckEmail.as_view()
        response = view(request)
        # assert that the email existed in the database
        self.assertTrue(response.data['exists'])

        request_2 = factory.post(reverse('core:check_email'), {'email': 'aooo@yahoo.com'}, format='json')
        force_authenticate(request_2, user=self.user)
        view_2 = CheckEmail.as_view()
        response_2 = view_2(request_2)
        # assert that the email does not exist in the database
        self.assertFalse(response_2.data['exists'])


class JoinCommunityTestCase(TestCase):
    """ Test JoinCommunity API view """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.restaurant_type = CommunityType.objects.create(value='restaurant')
        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')

    def test_join_community(self) -> None:
        """ Check that joining a community works smoothly """
        factory = APIRequestFactory()

        request = factory.post(reverse('core:join_community'), {'key': self.test_community.key}, format='json')
        force_authenticate(request, user=self.user)
        view = JoinCommunity.as_view()
        view(request)
        # assert that user is a member of the community after joining
        self.assertIn(self.user, self.test_community.members.all())

    def test_join_community_errors(self) -> None:
        """ Check that joining a community errors properly """
        factory = APIRequestFactory()
        # try with the wrong key
        request_2 = factory.post(reverse('core:join_community'), {'key': 'wrong_key'}, format='json')
        force_authenticate(request_2, user=self.user)
        view_2 = JoinCommunity.as_view()
        response_2 = view_2(request_2)
        # assert that user is not a member of the community after joining
        self.assertTrue('key' in response_2.data)
        self.assertEqual(response_2.data['key'], 'Incorrect key')
        self.assertNotIn(self.user, self.test_community.members.all())

        # try without key
        request_3 = factory.post(reverse('core:join_community'))
        force_authenticate(request_3, user=self.user)
        view_3 = JoinCommunity.as_view()
        response_3 = view_3(request_3)
        # assert that user is not a member of the community after joining
        self.assertTrue('key' in response_3.data)
        self.assertEqual(response_3.data['key'], 'Enter a key')
        self.assertNotIn(self.user, self.test_community.members.all())


class LeaveCommunityTestCase(TestCase):
    """ Test LeaveCommunity API view """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.restaurant_type = CommunityType.objects.create(value='restaurant')
        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')

        self.test_community.members.add(self.user)

    def test_leave_community(self) -> None:
        """ Check that leaving a community works smoothly """
        factory = APIRequestFactory()

        request = factory.post(reverse('core:leave_community'), {'community': self.test_community.pk}, format='json')
        force_authenticate(request, user=self.user)
        view = LeaveCommunity.as_view()
        view(request)
        # assert that user is no longer a member of the community after leaving
        self.assertNotIn(self.user, self.test_community.members.all())

    def test_leave_community_errors(self) -> None:
        """ Check that leaving a community errors properly """
        factory = APIRequestFactory()
        # try with the wrong community id - using some random number
        request_2 = factory.post(reverse('core:leave_community'), {'community': '83292898328382893'}, format='json')
        force_authenticate(request_2, user=self.user)
        view_2 = LeaveCommunity.as_view()
        response_2 = view_2(request_2)
        # assert that user is still a member of the community after leaving
        self.assertTrue('community' in response_2.data)
        self.assertEqual(response_2.data['community'], 'Community does not exist')
        self.assertIn(self.user, self.test_community.members.all())

        # try without community
        request_3 = factory.post(reverse('core:leave_community'))
        force_authenticate(request_3, user=self.user)
        view_3 = LeaveCommunity.as_view()
        response_3 = view_3(request_3)
        # assert that user is still a member of the community after leaving
        self.assertTrue('community' in response_3.data)
        self.assertEqual(response_3.data['community'], 'Enter a community')
        self.assertIn(self.user, self.test_community.members.all())


class RemoveFeatureTestCase(TestCase):
    """ Test RemoveFeature API view """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.restaurant_type = CommunityType.objects.create(value='restaurant')

        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')
        self.test_feature = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)

        self.test_community.features.add(self.test_feature)
        self.test_community.admins.add(self.user)

    def test_remove_feature(self) -> None:
        """ Check that removing a feature from a community works smoothly """
        factory = APIRequestFactory()

        request = factory.post(reverse('core:remove_feature'),
                               {'community': self.test_community.pk, 'feature': self.test_feature.pk},
                               format='json')
        force_authenticate(request, user=self.user)
        view = RemoveFeature.as_view()
        view(request)
        # assert that feature is no longer in the community after removing
        self.assertNotIn(self.test_feature, self.test_community.features.all())

    def test_remove_feature_errors(self) -> None:
        """ Check that removing a feature from a community errors properly """
        factory = APIRequestFactory()

        # try with the wrong community id - using some random number
        request_2 = factory.post(reverse('core:remove_feature'),
                                 {'community': '83292898328382893', 'feature': '29893893'},
                                 format='json')
        force_authenticate(request_2, user=self.user)
        view_2 = RemoveFeature.as_view()
        response_2 = view_2(request_2)
        # assert that feature is still in the community after removing
        self.assertTrue('community' in response_2.data)
        self.assertEqual(response_2.data['community'], 'Community does not exist')
        self.assertIn(self.test_feature, self.test_community.features.all())

        # try without community
        request_3 = factory.post(reverse('core:remove_feature'))
        force_authenticate(request_3, user=self.user)
        view_3 = RemoveFeature.as_view()
        response_3 = view_3(request_3)
        # assert that feature is still in the community after removing
        self.assertTrue('community' in response_3.data)
        self.assertEqual(response_3.data['community'], 'Enter a community')
        self.assertIn(self.test_feature, self.test_community.features.all())


class AddFeatureToCommunityTestCase(TestCase):
    """ Test AddFeatureToCommunity API view """

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='alice', password="alice2$$$")
        self.restaurant_type = CommunityType.objects.create(value='restaurant')

        self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
                                                       picture='', description='')
        self.test_feature = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)

        self.test_community.admins.add(self.user)

    def test_add_feature(self) -> None:
        """ Check that adding a feature to a community works smoothly """
        factory = APIRequestFactory()

        request = factory.post(reverse('core:add_feature_to_community'),
                               {'community': self.test_community.pk, 'feature': self.test_feature.pk},
                               format='json')
        force_authenticate(request, user=self.user)
        view = AddFeatureToCommunity.as_view()
        view(request)
        # assert that feature is no longer in the community after removing
        self.assertIn(self.test_feature, self.test_community.features.all())

    def test_add_feature_errors(self) -> None:
        """ Check that adding a feature to a community errors properly """
        factory = APIRequestFactory()

        # try with the wrong community id - using some random number
        request_2 = factory.post(reverse('core:add_feature_to_community'),
                                 {'community': '83292898328382893', 'feature': '29893893'},
                                 format='json')
        force_authenticate(request_2, user=self.user)
        view_2 = AddFeatureToCommunity.as_view()
        response_2 = view_2(request_2)
        # assert that feature is not in the community after removing
        self.assertTrue('community' in response_2.data)
        self.assertEqual(response_2.data['community'], 'Community does not exist')
        self.assertNotIn(self.test_feature, self.test_community.features.all())

        # try without community
        request_3 = factory.post(reverse('core:add_feature_to_community'))
        force_authenticate(request_3, user=self.user)
        view_3 = AddFeatureToCommunity.as_view()
        response_3 = view_3(request_3)
        # assert that feature is not in the community after removing
        self.assertTrue('community' in response_3.data)
        self.assertEqual(response_3.data['community'], 'Enter a community')
        self.assertNotIn(self.test_feature, self.test_community.features.all())


class DataStoreTestCase(TestCase):
    """

    Test DataStore API view

    Notes
    -----
    Implementation commented because it can only be tested with a Postgres database
    because the model uses a Postgres only field. It was tested manually. Due to Heroku
    free Postgres server limitation, the test database is SQLite.

    """

    # def setUp(self) -> None:
    #     self.user = User.objects.create_user(username='alice', password="alice2$$$")
    #     self.restaurant_type = CommunityType.objects.create(value='restaurant')
    #
    #     self.test_community = Community.objects.create(name='test', type=self.restaurant_type,
    #                                                    picture='', description='')
    #     self.test_feature = Feature.objects.create(name='test', description='', picture='', payload='', user=self.user)
    #
    #     self.test_community.features.add(self.test_feature)
    #     self.test_community.admins.add(self.user)
    #
    #     self.user_store = SimpleStore.objects.create(feature=self.test_feature, key='test',
    #                                                  value='', user=self.user, community=self.test_community,
    #                                                  access=DataAccessType.USER)
    #     self.admin_store = SimpleStore.objects.create(feature=self.test_feature, key='test',
    #                                                   value='', user=self.user, community=self.test_community,
    #                                                   access=DataAccessType.ADMIN)
    #     self.community_store = SimpleStore.objects.create(feature=self.test_feature, key='test',
    #                                                       value='', user=self.user, community=self.test_community,
    #                                                       access=DataAccessType.COMMUNITY)

    # def test_get_request(self) -> None:
    #     """ Check that get request returns the appropriate SimpleStore objects """
    #     factory = APIRequestFactory()
    #
    #     request = factory.post(reverse('core:data_store'),
    #                            {'mega$tag': 'test',
    #                             'mega$community': self.test_community.pk,
    #                             'mega$feature': self.test_feature.pk},
    #                            format='json')
    #     force_authenticate(request, user=self.user)
    #     view = AddFeatureToCommunity.as_view()
    #     response = view(request)
    #     # assert the stores returned are the appropriate stores
    #     print(response.data)
    #     # self.assertEqual()