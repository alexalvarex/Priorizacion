# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-27 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0024_remove_comunidad_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='comunidad',
            name='des',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Tiene_Escuela', to='admini.Descicion'),
            preserve_default=False,
        ),
    ]