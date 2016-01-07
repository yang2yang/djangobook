#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""djangobook URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',views.hello),#第一个参数是配置的ur路径，第二个参数是视图文件的函数（作为一个参数传递过去）
    url(r'^$',views.hello),      #根目录的路径的配置
    url(r'^time/$',views.current_datetime),
    url(r'^time/plus/(\d+)/$',views.hours_ahead),#有参数的路径配置，可以查出来如何将参数传递给视图
    url(r'^time/tem$',views.current_datetime_tem)
]
