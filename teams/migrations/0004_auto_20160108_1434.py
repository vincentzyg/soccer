# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20160108_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamsinfo',
            name='country_code',
            field=models.IntegerField(),
        ),
    ]