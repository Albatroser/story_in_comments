# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 13:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story_posting', '0003_auto_20161029_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='is_posted',
        ),
    ]
