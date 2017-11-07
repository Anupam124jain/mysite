# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-03 08:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=30, unique=True)),
                ('student_name', models.CharField(max_length=30)),
                ('password', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='student_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherStudentFeedback.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=30, unique=True)),
                ('teacher_name', models.CharField(max_length=30)),
                ('student_rating', models.IntegerField(default=None)),
                ('student_remarks', models.CharField(default=None, max_length=50)),
                ('password', models.CharField(default=None, max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='student_teacher',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeacherStudentFeedback.Teacher'),
        ),
    ]