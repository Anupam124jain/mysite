# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from OnlineFeeSystem.models import *

@admin.register(StudentInfo)
class StudentInfo(admin.ModelAdmin):
    pass

@admin.register(FeeStructure)
class FeeStructure(admin.ModelAdmin):
    pass

@admin.register(StudentFeeInfo)
class StudentFeeInfo(admin.ModelAdmin):
    pass

@admin.register(FeeStatus)
class FeeStatus(admin.ModelAdmin):
    pass


