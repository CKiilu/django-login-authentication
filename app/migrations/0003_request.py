# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-08 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_profile_pictures_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
