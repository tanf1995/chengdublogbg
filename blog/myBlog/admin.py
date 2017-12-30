# coding=utf-8
from django.contrib import admin
from .models import Classify, Article, Message, Record

admin.site.register(Classify)
admin.site.register(Article)
admin.site.register(Message)
admin.site.register(Record)


