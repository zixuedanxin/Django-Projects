# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-11 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relapp', '0003_auto_20180911_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='student',
            field=models.OneToOneField(on_delete=models.SET(20), to='relapp.Student'),
        ),
    ]