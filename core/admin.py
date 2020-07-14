from django.contrib import admin

from .models import Profile, Community, Feature, Database

# Register your models here

admin.register(Profile)
admin.register(Community)
admin.register(Feature)
admin.register(Database)