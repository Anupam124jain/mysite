# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeacherStudentFeedback', '0004_auto_20171103_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_rating',
            field=models.IntegerField(choices=[(b'one', b'1'), (b'two', b'2'), (b'three', b'3'), (b'four', b'4'), (b'five', b'5')], null=True),
        ),
    ]
