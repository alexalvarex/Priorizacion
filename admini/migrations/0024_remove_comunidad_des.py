# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-27 01:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0023_auto_20171126_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comunidad',
            name='des',
        ),
    ]
