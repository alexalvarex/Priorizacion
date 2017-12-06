# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-21 17:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admini', '0018_auto_20171121_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priorizar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoragua', models.IntegerField(null=True)),
                ('valorruta', models.IntegerField(null=True)),
                ('valortone', models.IntegerField(null=True)),
                ('valorproce', models.IntegerField(null=True)),
                ('valorqmi', models.IntegerField(null=True)),
                ('valorpi', models.IntegerField(null=True)),
                ('comunidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admini.Comunidad')),
            ],
        ),
    ]
