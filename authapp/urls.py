from django.urls import re_path
import authapp.views as authapp

# Required for Django 2.0 and above
app_name = 'authapp'

urlpatterns = [
    re_path('^login/$', authapp.login , name='login'),
    re_path('^logout/$', authapp.logout, name='logout'),
    ]
