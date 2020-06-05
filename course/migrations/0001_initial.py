# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_no', models.CharField(max_length=255)),
                ('title_tw', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('credit', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Deparment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]