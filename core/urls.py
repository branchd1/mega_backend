from django.urls import path, include

from core import views

app_name = 'core'

urlpatterns = [
	path('check_email/', views.CheckEmail.as_view(), name='check_email'),
	path('communities/join/', views.JoinCommunity.as_view(), name='join_community'),
	path('features/add_to_community/', views.AddFeatureToCommunity.as_view(), name='add_feature_to_community'),
	path('data_store/', views.DataStore.as_view(), name='data_store'),
]
