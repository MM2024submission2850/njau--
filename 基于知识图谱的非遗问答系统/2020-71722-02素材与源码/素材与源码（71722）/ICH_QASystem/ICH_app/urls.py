# @Time : 2020/3/15 9:19 
# @Author : FAN_Y
#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from django.conf.urls import url
from ICH_app import views    #尽管会画红线，但无碍

urlpatterns=[
url(r'query', views.query),
]