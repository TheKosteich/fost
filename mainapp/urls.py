from django.urls import re_path
import mainapp.views as mainapp

# Required for Django 2.0 and above
app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.products, name='index'),
    re_path(r'^(\d+)/$', mainapp.products, name='category'),
]
