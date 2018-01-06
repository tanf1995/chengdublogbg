# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='article',
            name='A_cover',
            field=models.ImageField(upload_to=b'articleImg'),
        ),
        migrations.AlterField(
            model_name='record',
            name='R_delete',
            field=models.BooleanField(default=False),
        ),
    ]
