# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_comment', '0004_comment_score_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_time',
            field=models.DateTimeField(default='2017-01-01'),
            preserve_default=False,
        ),
    ]