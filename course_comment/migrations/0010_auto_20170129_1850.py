# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_comment', '0009_auto_20170129_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='hardness',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sweety',
            field=models.IntegerField(default=0),
        ),
    ]