# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestTinymce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.TextField(default=b'', verbose_name=b'\xe6\x96\x87\xe6\x9c\xac')),
            ],
            options={
                'db_table': 'test_tinymce',
                'verbose_name': '\u6d4b\u8bd5',
                'verbose_name_plural': '\u6d4b\u8bd5',
            },
        ),
    ]
