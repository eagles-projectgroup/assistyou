from django.urls import path
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib import admin
from . import views

app_name = 'custom_auth'

urlpatterns = [
    path('', views.main, name='main'),
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='custom_auth/password_reset_done.html'),
         name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='custom_auth/password_reset_confirm.html',
                                          success_url='/custom_auth/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='custom_auth/password_reset_complete.html'),
         name='password_reset_complete')
]