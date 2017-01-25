# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20161103114236 on 2017-01-19 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_name', models.CharField(max_length=200)),
                ('student_class', models.CharField(max_length=1)),
                ('student_number', models.IntegerField()),
                ('system_programming', models.BooleanField(default=True)),
                ('has_document', models.BooleanField(default=False)),
                ('has_assignment', models.BooleanField(default=False)),
                ('has_commission', models.BooleanField(default=False)),
                ('has_reviewer', models.BooleanField(default=False)),
            ],
        ),
    ]
