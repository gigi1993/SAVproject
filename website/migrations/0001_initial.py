# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-11 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('click_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ip_address', models.CharField(default='defaultIP', max_length=120)),
                ('clicked', models.CharField(default='country', max_length=10)),
            ],
        ),
    ]
