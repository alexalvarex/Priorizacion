# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-22 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0021_remove_priorizar_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='priorizar',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
