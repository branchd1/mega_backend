"""
mega_backend URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core import views

# DRF router configuration

api_router = routers.DefaultRouter()
api_router.register(r'profiles', views.ProfileViewSet, basename='profile')
api_router.register(r'features', views.FeatureViewSet, basename='feature')
api_router.register(r'databses', views.DatabaseViewSet, basename='database')
api_router.register(r'communities', views.CommunityViewSet, basename='community')

# the urls

urlpatterns = [
	path('api/', include(api_router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
]
