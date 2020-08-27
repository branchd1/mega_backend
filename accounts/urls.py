from django.urls import path

from django.contrib.auth import views as auth_views

from accounts.forms import MySetPasswordForm

app_name = 'accounts'

urlpatterns = [
    path('password/reset/confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='accounts/registration/my_password_reset_confirm.html',
             form_class=MySetPasswordForm
         ),
         name='password_reset_confirm'),
    path('password/reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
