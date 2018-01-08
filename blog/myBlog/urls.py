# coding=utf-8
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^about/$', views.about, name='about'),
    url('^life/$', views.life, name='life'),
    url('^messages/$', views.messages, name='messages'),
    url('^messagesHandler/$', views.messageHandler, name='messagesHandler'),
    url('^technique/$', views.technique, name='technique'),
    url('^feeling/$', views.feeling, name='feeling'),
    url('^time/$', views.time, name='time'),
    url('^article/(?P<id>[0-9]+)/$', views.article, name='article'),
    url(r'^upload_img/$', views.upload_img)  # 后台富文本框上传图片
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)