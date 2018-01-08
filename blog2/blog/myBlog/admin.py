# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Classify, Article, Message, Record


class ArticleTinymce_Admin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/tinymce/js/jquery-3.2.1.min.js',  # 必须首先加载的jquery，手动添加文件
            '/static/tinymce/js/tinymce/tinymce.min.js',  # tinymce自带文件
            '/static/tinymce/js/tinymce/plugins/jquery.form.js',  # 手动添加文件
            '/static/tinymce/js/tinymce/textarea.js',  # 手动添加文件，用户初始化参数
        ]


admin.site.register(Classify)
admin.site.register(Article, ArticleTinymce_Admin)
admin.site.register(Message)
admin.site.register(Record)
