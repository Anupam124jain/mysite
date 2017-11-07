# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class StudentInfo(models.Model):
    enroll_id = models.CharField(max_length = 30,unique=True)
    enroll_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    student_name = models.CharField(max_length = 100)
    fathers_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length=100)
    branch = models.CharField(max_length = 50)
    mobile_no = models.IntegerField()
    fees_status = models.BooleanField()
    student_type = models.CharField(max_length = 50)
    sem = models.IntegerField()

    def __str__(self):
        return self.enroll_id


class FeeStructure(models.Model):
    year = models.CharField(max_length=50)
    sem_fee = models.IntegerField()
    hostel_fee = models.IntegerField()
    bus_fee = models.IntegerField()
    mess_fee = models.IntegerField()
    late_fee = models.IntegerField()

    def __str__(self):
        return self.id

class StudentFeeInfo(models.Model):
    student = models.ForeignKey(StudentInfo)
    fee = models.ForeignKey(FeeStructure)

    def __str__(self):
        return self.id


class FeeStatus(models.Model):
    student = models.ForeignKey(StudentInfo)
    sem = models.IntegerField()
    sem_fee_status = models.BooleanField()
    hostel_fee_status = models.CharField(max_length = 50)
    bus_fee_status = models.CharField(max_length = 50)
    mess_fee_status = models.CharField(max_length = 50)
    late_fee_status = models.CharField(max_length = 50)
    deposit_time = models.DateTimeField()

    def __str__(self):
        return self.student