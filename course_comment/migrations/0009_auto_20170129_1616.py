# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_comment', '0008_comment_score_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='cold',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='hardness',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sweety',
            field=models.FloatField(default=0),
        ),
    ]