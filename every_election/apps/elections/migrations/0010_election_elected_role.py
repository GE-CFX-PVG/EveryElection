# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0009_auto_20161101_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='election',
            name='elected_role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='elections.ElectedRole'),
        ),
    ]