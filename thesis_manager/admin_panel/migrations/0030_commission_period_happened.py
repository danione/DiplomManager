# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161103114236 on 2017-02-27 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0029_thesis_period_given'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='period_happened',
            field=models.CharField(default='2017-2018', max_length=15),
        ),
    ]
