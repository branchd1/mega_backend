from django.urls import path, include

from core import views

app_name = 'core'

urlpatterns = [
	path('check_email/', views.CheckEmail.as_view(), name='check_email'),
]