from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('check_email/', views.CheckEmail.as_view(), name='check_email'),
    path('communities/join/', views.JoinCommunity.as_view(), name='join_community'),
    path('communities/leave/', views.LeaveCommunity.as_view(), name='leave_community'),
    path('features/add_to_community/', views.AddFeatureToCommunity.as_view(), name='add_feature_to_community'),
    path('features/remove/', views.RemoveFeature.as_view(), name='remove_feature'),
    path('data_store/', views.DataStore.as_view(), name='data_store'),
    path('data_store_delete/<int:store_id>/', views.DataStoreDelete.as_view(), name='data_store_delete'),
    path('upload_img/', views.UploadImage.as_view(), name='upload_img'),
]