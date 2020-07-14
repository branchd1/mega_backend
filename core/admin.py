from django.contrib import admin

from .models import Profile, Community, Feature, Database

# Register your models here

admin.site.register(Profile)
admin.site.register(Community)
admin.site.register(Feature)
admin.site.register(Database)