""" This module is used to register models in the built in Django admin console """

from django.contrib import admin

from core.models import Community, Feature, SimpleStore, UploadedImage, CommunityType

# Register models

admin.site.register(Community)
admin.site.register(Feature)
admin.site.register(SimpleStore)
admin.site.register(UploadedImage)
admin.site.register(CommunityType)
