# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-30 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0026_auto_20171129_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='priorizar',
            name='comunidad',
        ),
        migrations.AddField(
            model_name='priorizar',
            name='comunidad',
            field=models.ManyToManyField(to='admini.Comunidad'),
        ),
    ]
