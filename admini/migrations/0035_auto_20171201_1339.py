# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-01 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0034_auto_20171201_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultados',
            name='total',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
    ]
