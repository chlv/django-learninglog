# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
