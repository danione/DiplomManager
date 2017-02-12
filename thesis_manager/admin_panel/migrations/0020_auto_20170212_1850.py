# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161103114236 on 2017-02-12 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0019_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='current_thesis',
        ),
        migrations.AddField(
            model_name='student',
            name='current_thesis',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.Thesis'),
        ),
    ]
