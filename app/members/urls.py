from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register_user'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name='authenticate/password_reset.html'),
          name='reset_password'),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name='authenticate/password_reset_sent.htnl'),
         name='reset_password_done'),
    path('reset/<uidb64>/<token>', 
         auth_views.PasswordResetConfirmView.as_view(template_name='authenticate/password_reset_form.html'), 
         name='password_reset_confirm'),
    path('reset_password_complete', 
         auth_views.PasswordResetCompleteView.as_view(template_name='authenticate/password_reset_done.html'), 
         name='password_reset_complete'),

     path('password', auth_views.PasswordChangeView.as_view(template_name='authenticate/change_password.html'), name='change_password')

]

