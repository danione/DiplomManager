# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161103114236 on 2017-02-11 16:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_auto_20170211_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='progress',
        ),
    ]
