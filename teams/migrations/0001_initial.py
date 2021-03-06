# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoachsInfo',
            fields=[
                ('coach_code', models.IntegerField(primary_key=True, serialize=False)),
                ('coach_name', models.CharField(max_length=30)),
                ('coach_country', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MatchesInfo',
            fields=[
                ('match_id', models.IntegerField(primary_key=True, serialize=False)),
                ('match_code', models.CharField(max_length=4)),
                ('team_home_goals', models.PositiveIntegerField()),
                ('team_away_goals', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlayersInfo',
            fields=[
                ('player_name', models.CharField(max_length=30)),
                ('player_code', models.IntegerField(primary_key=True, serialize=False)),
                ('player_loc', models.CharField(max_length=30)),
                ('player_height', models.PositiveIntegerField()),
                ('co_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.CoachsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Relationship_Sponsors_teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_of_sponsor', models.IntegerField()),
                ('years_of_contract', models.IntegerField()),
                ('loc_of_contract', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorsInfo',
            fields=[
                ('sponsor_name', models.CharField(max_length=30)),
                ('nasdaq', models.IntegerField(primary_key=True, serialize=False)),
                ('loc_of_sponsor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TeamsInfo',
            fields=[
                ('team_code', models.IntegerField(primary_key=True, serialize=False)),
                ('country_name', models.CharField(max_length=30)),
                ('country_code', models.CharField(max_length=30)),
                ('total_score', models.PositiveIntegerField()),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.MatchesInfo')),
            ],
        ),
        migrations.AddField(
            model_name='sponsorsinfo',
            name='sponsor_team',
            field=models.ManyToManyField(through='teams.Relationship_Sponsors_teams', to='teams.TeamsInfo'),
        ),
        migrations.AddField(
            model_name='relationship_sponsors_teams',
            name='sp_nas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.SponsorsInfo'),
        ),
        migrations.AddField(
            model_name='relationship_sponsors_teams',
            name='t_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamsInfo'),
        ),
        migrations.AddField(
            model_name='playersinfo',
            name='team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamsInfo'),
        ),
        migrations.AddField(
            model_name='coachsinfo',
            name='coach_team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamsInfo'),
        ),
    ]
