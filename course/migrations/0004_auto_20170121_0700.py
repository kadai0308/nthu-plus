# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 07:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_deparment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='deparment',
            new_name='department',
        ),
    ]
