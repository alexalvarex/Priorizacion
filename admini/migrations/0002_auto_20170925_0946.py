# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-25 15:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('admini', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personas',
            name='usuario',
        ),
        migrations.AddField(
            model_name='colaborador',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Persona', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
