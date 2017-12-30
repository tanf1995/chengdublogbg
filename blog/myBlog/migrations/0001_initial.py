# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('A_author', models.CharField(max_length=100)),
                ('A_pubTime', models.DateField(auto_now_add=True)),
                ('A_title', models.CharField(max_length=400)),
                ('A_clickNum', models.IntegerField(default=0)),
                ('A_keyword', models.CharField(max_length=100, null=True, blank=True)),
                ('A_cover', models.ImageField(upload_to=b'')),
                ('A_content', tinymce.models.HTMLField()),
                ('A_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('C_name', models.CharField(max_length=100)),
                ('C_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('M_author', models.CharField(max_length=100)),
                ('M_content', models.CharField(max_length=4000)),
                ('M_delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('R_pubTime', models.DateField(auto_now_add=True)),
                ('R_content', models.CharField(max_length=4000)),
                ('R_delete', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='A_classify',
            field=models.ForeignKey(to='myBlog.Classify'),
        ),
    ]
