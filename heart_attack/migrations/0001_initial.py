# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StoreData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField()),
                ('cp_type', models.IntegerField()),
                ('trest_bps', models.IntegerField()),
                ('Chol', models.IntegerField()),
                ('fbs', models.IntegerField()),
                ('rer', models.IntegerField()),
                ('thalch', models.IntegerField()),
                ('eia', models.IntegerField()),
                ('oldpeak', models.IntegerField()),
                ('slpe', models.IntegerField()),
                ('ca', models.IntegerField()),
                ('thal', models.IntegerField()),
                ('ads', models.IntegerField()),
            ],
        ),
    ]
