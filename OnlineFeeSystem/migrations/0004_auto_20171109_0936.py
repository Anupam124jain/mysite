# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineFeeSystem', '0003_auto_20171108_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='mobile_no',
            field=models.CharField(max_length=15),
        ),
    ]