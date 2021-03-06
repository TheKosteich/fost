"""fost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
import mainapp.views as mainapp
#
# Only for development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('^$', mainapp.index, name='index'),
    re_path('^bouquets/$', mainapp.products, name='products'),
    # re_path('^bouquets/', include('mainapp.urls', namespace='products')),
    # re_path('^bouquet/$', mainapp.bouquet, name='bouquet'),
    re_path('^compositions/$', mainapp.compositions, name='compositions'),
    re_path('^wedding/$', mainapp.wedding, name='wedding'),
    re_path('^interior/$', mainapp.interior, name='interior'),
    re_path('^blog/$', mainapp.blog, name='blog'),
    re_path('^friends/$', mainapp.friends, name='friends'),
    re_path('^contacts/$', mainapp.contacts, name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
