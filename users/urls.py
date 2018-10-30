"""django_test URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from users import views as uviews

urlpatterns = [

    url(r'^index/$', uviews.index),

    url(r'^news/$', uviews.news),

    url(r'^headers/$', uviews.getheader),

    url(r'^resp/$', uviews.common_resp),

    url(r'^jresp/$', uviews.json_resp),

    url(r'^redirect/$', uviews.redirect_page),

    url(r'^setcookie/$', uviews.set_cookie),
    url(r'^getcookie/$', uviews.get_cookie),

    url(r'^setsession/$', uviews.set_session),
    url(r'^getsession/$', uviews.get_session),
]
