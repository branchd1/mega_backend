from django.urls import path

from developer import views

app_name = 'developer'

urlpatterns = [
    path('', views.index, name='home'),
]
