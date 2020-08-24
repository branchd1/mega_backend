"""
mega_backend URL Configuration

The `urlpatterns` list routes URLs to views
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from core import views as core_views, urls as core_urls

from django.conf.urls.static import static
from django.conf import settings

# DRF router configuration

api_router = routers.DefaultRouter()
api_router.register(r'profiles', core_views.ProfileViewSet, basename='profile')
api_router.register(r'features', core_views.FeatureViewSet, basename='feature')
api_router.register(r'simplestores', core_views.SimpleStoreViewSet, basename='simplestore')
# api_router.register(r'liststores', core_views.ListStoreViewSet, basename='liststore')
# api_router.register(r'mapstores', core_views.MapStoreViewSet, basename='mapstore')
api_router.register(r'communities', core_views.CommunityViewSet, basename='community')

# the urls

urlpatterns = \
    [
        path('api/', include(core_urls)),
        path('api/', include(api_router.urls)),
        path('admin/', admin.site.urls),
        path('auth/', include('djoser.urls')),
        path('auth/', include('djoser.urls.authtoken')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
