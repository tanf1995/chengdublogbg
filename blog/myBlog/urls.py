# coding=utf-8
from django.conf.urls import include, url
import views

urlpatterns = [
    url('^$', views.index, name='index'),

]