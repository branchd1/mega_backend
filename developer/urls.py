"""
This module specifies the developer website URLs and determines what views to match with them

"""

from django.urls import path

from developer import views

app_name = 'developer'

urlpatterns = [
    path('', views.index, name='index'),
    path('add-feature/', views.add_feature, name='add_feature'),
    path('edit-feature/<int:feature_id>/', views.edit_feature, name='edit_feature'),
    path('feature-details/<int:feature_id>/', views.feature_details, name='feature_details'),
    path('delete-feature/<int:feature_id>/', views.delete_feature, name='delete_feature'),
]
