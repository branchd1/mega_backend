from django.contrib import admin

from .models import Community, Feature, SimpleStore, UploadedImage

# Register models

admin.site.register(Community)
admin.site.register(Feature)
admin.site.register(SimpleStore)
admin.site.register(UploadedImage)
