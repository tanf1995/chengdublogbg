# coding=utf-8
from django.conf.urls import include, url
import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^about/$', views.about, name='about'),
    url('^life/$', views.life, name='life'),
    url('^messages/$', views.messages, name='messages'),
    url('^technique/$', views.technique, name='technique'),
    url('^feeling/$', views.feeling, name='feeling'),
    url('^time/$', views.time, name='time'),
    url('^article/(?P<id>[0-9]+)/$', views.article, name='article')  # 单片文章，后来修改
]