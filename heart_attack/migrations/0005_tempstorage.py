# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart_attack', '0004_auto_20180324_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempstorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]