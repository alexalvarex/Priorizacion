# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-02 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0008_auto_20171102_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbasAgua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agua', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='comunidad',
            name='agua',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Abastecimiento_Agua', to='admini.AbasAgua'),
            preserve_default=False,
        ),
    ]