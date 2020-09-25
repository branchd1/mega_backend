import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mega_backend.settings")

import django
django.setup()

from django.conf import settings
from django.contrib.auth.models import User
from core.models import Feature, Community, CommunityType

menu_feature = '{"admin":{"home":{"metadata":{"show_back_button":"false"},"components":[{"button":{"value":"manage ' \
               'items","action":{"action_type":"change_page","new_page":"manage_items"}}},{"grid":{"action":{' \
               '"action_type":"get","tag":"menu","add_page":{"new_page":"add_menu"},"search":{"field":"item_name"}},' \
               '"title":{"value":"mega$action$value.item_name","prefix":"item: "},"subtitle":{' \
               '"value":"mega$action$value.item_price","prefix":"price: $"},"image":{' \
               '"value":"mega$action$value.item_picture"},"empty_text":{"value":"No items"},"empty_subtext":{' \
               '"value":"add below"},"error_text":{"value":"Cannot retrieve communities"},"error_subtext":{' \
               '"value":"Try again"}}}]},"manage_items":{"components":[{"list":{"action":{"action_type":"get",' \
               '"tag":"menu","delete":{"new_page":"manage_items"}},"title":{"value":"mega$action$value.item_name"},' \
               '"subtitle":{"value":"mega$action$value.item_price","prefix":"price: $"},"empty_text":{"value":"No ' \
               'items"}}}]},"add_menu":{"components":[{"form":{"action":{"action_type":"save","multipart":[{' \
               '"field":"item_picture"}],"method":"post","access":"community","tag":"menu"},"body":[{"stuffing":{' \
               '"height":"20"}},{"input":{"type":"text","name":"item_name","hint":"item name *","validators":{' \
               '"required":""}}},{"stuffing":{"height":"20"}},{"input":{"type":"text","name":"item_price",' \
               '"hint":"item price *","validators":{"required":"","number":""}}},{"stuffing":{"height":"20"}},' \
               '{"input":{"type":"file","name":"item_picture","hint":"item picture *","validators":{"required":"",' \
               '"max_file_size":"2.0"}}},{"button":{"type":"submit","value":"submit","action":{' \
               '"action_type":"change_page","new_page":"home"}}}]}}]}},"member":{"home":{"components":[{"list":{' \
               '"action":{"action_type":"get","tag":"menu"},"title":{"value":"mega$action$value.item_name"},' \
               '"subtitle":{"value":"mega$action$value.item_price","prefix":"price: $"},"empty_text":{"value":"No ' \
               'items"}}}]}}} '

users = [
    {
        'email': 'mega.app.project.2020@gmail.com',
        'password': 'MegaAppPassword$',
        'first_name': 'John',
        'last_name': 'Doe'
    }, {
        'email': 'dummy-email@gmail.com',
        'password': 'MegaAppPassword$',
        'first_name': 'Alice',
        'last_name': 'Bob'
    }
]

for user in users:
    User.objects.create_user(username=user['email'], email=user['email'], password=user['password'],
                             first_name=user['first_name'], last_name=user['last_name'])

features = [
    {
        'name': 'Menu Feature',
        'description': 'A menu feature to order food items in a restaurant community',
        'payload': menu_feature,
        'user': User.objects.get(username=users[0]['email']),
        'picture': 'pop_script/menu_feature.png'
    }
]

for feature in features:
    Feature.objects.create(name=feature['name'], description=feature['description'],
                           payload=feature['payload'], user=feature['user'], picture=feature['picture'])

community_types = [
    {
        'value': 'restaurant'
    },
]

for community_type in community_types:
    CommunityType.objects.create(value=community_type['value'])

communities = [
    {
        'name': 'Restaurant 54',
        'type': CommunityType.objects.get(value=community_types[0]['value']),
        'description': 'This is the community MiniApp for the Restaurant 54 brand',
        'picture': 'pop_script/restaurant_logo.png'
    }
]

for community in communities:
    community_object = Community.objects.create(name=community['name'], type=community['type'],
                                                description=community['description'],
                                                picture=community['picture'])
    community_object.admins.add(User.objects.get(username=users[0]['email']))
    community_object.members.add(User.objects.get(username=users[1]['email']))
    community_object.features.add(Feature.objects.get(name=features[0]['name']))

