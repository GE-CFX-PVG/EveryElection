# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-28 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisations', '0008_organisationdivision_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisationdivision',
            name='division_election_sub_type',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
