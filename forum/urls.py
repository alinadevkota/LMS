# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from django.urls import path
from . import api
from . import views

app_name = "forum"
api_router = routers.DefaultRouter()
api_router.register(r'threads', api.ThreadApiView)
api_router.register(r'post', api.PostApiView)

urlpatterns = [
    path(r'^page/(?P<page>[0-9]+)/$', views.Index.as_view(), name='index'),
    path(r'^$', views.Index.as_view(), name='index'),
    path(r'^topic/(?P<pk>\d+)/page/(?P<page>[0-9]+)/$', views.TopicView.as_view(), name='topic'),
    path(r'^topic/(?P<pk>\d+)/$', views.TopicView.as_view(), name='topic'),
    path(r'^n/(?P<pk>\d+)/page/(?P<page>[0-9]+)/$', views.NodeGroupView.as_view(), name='nodegroup'),
    path(r'^n/(?P<pk>\d+)/$', views.NodeGroupView.as_view(), name='nodegroup'),
    url(r'^t/(?P<pk>\d+)/edit/$', views.edit_thread, name='edit_thread'),
    url(r'^t/(?P<pk>\d+)/append/$', views.create_appendix, name='create_appendix'),
    path(r'^t/(?P<pk>\d+)/page/(?P<page>[0-9]+)/$', views.ThreadView.as_view(), name='thread'),
    path(r'^t/(?P<pk>\d+)/$', views.ThreadView.as_view(), name='thread'),
    url(r'^u/(?P<pk>\d+)/$', views.user_info, name='user_info'),
    path(r'^u/(?P<pk>\d+)/threads/page/(?P<page>[0-9]+)/$', views.UserThreads.as_view(), name='user_threads'),
    path(r'^u/(?P<pk>\d+)/threads/$', views.UserThreads.as_view(), name='user_threads'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^reg/$', views.reg_view, name='reg'),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^search/$', views.search_redirect, name='search_redirect'),
    path(r'^search/(?P<keyword>.*?)/page/(?P<page>[0-9]+)/$', views.SearchView.as_view(), name='search'),
    path(r'^search/(?P<keyword>.*?)/$', views.SearchView.as_view(), name='search'),
    url(r'^t/create/$', views.create_thread, name='create_thread'),
    path(r'^notifications/$', views.NotificationView.as_view(), name='notifications'),
    url(r'^avatar/$', views.upload_avatar, name="upload_avatar"),
    url(r'^api/', include(api_router.urls)),
]
