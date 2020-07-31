"""
mega_backend URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core import views as core_views, urls as core_urls

# DRF router configuration

api_router = routers.DefaultRouter()
api_router.register(r'profiles', core_views.ProfileViewSet, basename='profile')
api_router.register(r'features', core_views.FeatureViewSet, basename='feature')
api_router.register(r'databases', core_views.DatabaseViewSet, basename='database')
api_router.register(r'communities', core_views.CommunityViewSet, basename='community')

# the urls

urlpatterns = [
	path('api/', include(core_urls)),
	path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
