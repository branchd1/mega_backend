"""
This module specifies core URLs for the backend REST API and determines what views to match with them

"""

from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('check-email/', views.CheckEmail.as_view(), name='check_email'),
    path('communities/join/', views.JoinCommunity.as_view(), name='join_community'),
    path('communities/leave/', views.LeaveCommunity.as_view(), name='leave_community'),
    path('features/add-to-community/', views.AddFeatureToCommunity.as_view(), name='add_feature_to_community'),
    path('features/remove/', views.RemoveFeature.as_view(), name='remove_feature'),
    path('data-store/', views.DataStore.as_view(), name='data_store'),
    path('data-store/delete/<int:store_id>/', views.DataStoreDetails.as_view(), name='data_store_delete'),
    path('upload-img/', views.UploadImage.as_view(), name='upload_img'),
]