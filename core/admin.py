from django.contrib import admin

from .models import Profile, Community, Feature, SimpleStore, UploadedImage#, ListStore, MapStore

# Register models

admin.site.register(Profile)
admin.site.register(Community)
admin.site.register(Feature)
admin.site.register(SimpleStore)
admin.site.register(UploadedImage)
# admin.site.register(ListStore)
# admin.site.register(MapStore)
