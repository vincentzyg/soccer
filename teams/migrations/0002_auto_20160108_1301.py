# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 05:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playersinfo',
            old_name='co_id',
            new_name='co',
        ),
        migrations.RenameField(
            model_name='playersinfo',
            old_name='team_id',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='relationship_sponsors_teams',
            old_name='sp_nas',
            new_name='sp',
        ),
        migrations.RenameField(
            model_name='relationship_sponsors_teams',
            old_name='t_id',
            new_name='t',
        ),
        migrations.RenameField(
            model_name='teamsinfo',
            old_name='m_id',
            new_name='m',
        ),
    ]
