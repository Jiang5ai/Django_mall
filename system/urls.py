# -*- coding: utf-8 -*-
# @Time    : 2021/1/11 19:35
# @Author  : JS
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from system import views

urlpatterns = [
    url(r'^news/', views.news_list, name='news_list'),
    url(r'^new/(?P<pk>\d+)/$', views.news_detail, name='news_detail'),

]
