# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-12-04 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0039_auto_20171204_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidad',
            name='tipo_quema',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admini.TipoQuema'),
        ),
    ]