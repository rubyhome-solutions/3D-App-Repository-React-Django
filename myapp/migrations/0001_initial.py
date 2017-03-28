# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('role', models.CharField(choices=[('A', 'Admin'), ('R', 'Reviewer'), ('U', 'User')], max_length=2)),
            ],
        ),
    ]