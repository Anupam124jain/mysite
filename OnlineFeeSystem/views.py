# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from TeacherStudentFeedback.forms import TeacherFeedbackForm,TeacherSignupForm, TeacherLoginForm
from OnlineFeeSystem.models import StudentInfo,FeeStructure, StudentFeeInfo,FeeStatus
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render


def StudentRegister(request):
    if request.method == 'POST':
        form =  TeacherSignupForm(request.POST)
        if form.is_valid():
            password = make_password(request.POST['password'])
            student_register = StudentInfo(student_name = request.POST['student_name'],
                                           fathers_name = request.POST['fathers_name'],
                                           email = request.POST['email'],
                                           password = password,
                                           branch = request.POST['branch'],
                                           mobile_no = request.POST['mobile_no'],
                                           fees_status = request.POST['fee_status'],
                                           student_type = request.POST['student_type'],
                                           sem = request.POST['sem']
                                       )
            student_register.save()

            return render(request, 'success.html')
        else:
            return render(request, 'signup.html')
    else:
        form =  TeacherSignupForm()
        return render(request, 'signup.html', {'form': form})

def TeacherLogin(request):
    if request.method == 'POST':
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            password = make_password(request.POST['password'])
            teacher_login = Teacher(teacher_id=request.POST['teacher_id'],
                                    password=password
                                       )
            teacher_login.save()

            return render(request, 'success.html')
        else:
            return render(request, 'login.html')
    else:
        form = TeacherLoginForm()
        return render(request, 'login.html', {'form': form})
