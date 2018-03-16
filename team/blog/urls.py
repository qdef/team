"""team URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
        url(r'^$', views.liste, name='blog'),
        url(r'^football/$', views.football, name='football'),
        url(r'^rugby/$', views.rugby, name='rugby'),
        url(r'^american/$', views.american, name='american'),
        url(r'create/$', views.create, name='create'),
        url(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
        url(r'^edit/(?P<pk>\d+)/$', views.edit , name='edit'),
        url(r'^careful_when_clicking_this_link!!!/(?P<pk>\d+)/$', views.delete , name='delete'),
        url(r'^user_error/$', views.user_error, name='user_error'),
	]
