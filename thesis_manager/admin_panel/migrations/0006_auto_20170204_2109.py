# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161103114236 on 2017-02-04 19:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0005_archive'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Archive',
        ),
        migrations.RenameField(
            model_name='reviewer',
            old_name='id',
            new_name='reviewer_id',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='id',
            new_name='student_id',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='id',
            new_name='teacher_id',
        ),
        migrations.RenameField(
            model_name='thesis',
            old_name='id',
            new_name='thesis_id',
        ),
    ]