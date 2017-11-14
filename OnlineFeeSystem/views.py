# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from OnlineFeeSystem.forms import Registration_Form, Login_form, Forgot_Password,reset_password_form
from OnlineFeeSystem.models import StudentInfo, FeeStructure, StudentFeeInfo, FeeStatus
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from OnlineFeeSystem.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage


def student_register(request):
    if request.method == 'POST':
        form = Registration_Form(request.POST)
        if form.is_valid():
            password = make_password(request.POST['password'])
            student_register = StudentInfo(
                enroll_id=get_random_string(length=10),
                student_name=request.POST['student_name'],
                fathers_name=request.POST['fathers_name'],
                email=request.POST['email'],
                password=password,
                branch=request.POST['branch'],
                mobile_no=request.POST['mobile_no'],
                student_type=request.POST['student_type'],
                sem=request.POST['sem'],
                enroll_time=datetime.datetime.now(),
                fees_status=0
            )
            student_register.save()
            student_register.token = account_activation_token.make_token(student_register)
            student_register.save()
            current_site = get_current_site(request)
            sub = 'Activate Your MySite Account'
            message = render_to_string('OnlineFeeSystem/account_activation_email.html', {
                'domain': str(current_site),
                'student': student_register.student_name,
                'your_enrollment_id': student_register.enroll_id,
                'token': account_activation_token.make_token(student_register)
            })
            to_email = request.POST['email']
            email = EmailMessage(subject=sub, body=message, to=[to_email])
            email.send()
            return redirect('account_activation_sent')
        else:
            return render(request, 'OnlineFeeSystem/student_registration.html')
    else:
        form = Registration_Form()
        return render(request, 'OnlineFeeSystem/student_registration.html', {'form': form})


def student_login(request):
    if request.method == 'POST':
        form = Login_form(request.POST)
        # print form.cleaned_data['form']
        if form.is_valid():
            enroll_id = form.cleaned_data['enroll_id']
            # print enroll_id
            student_login = StudentInfo.objects.get(enroll_id=enroll_id)
            if check_password(request.POST.get('password'), student_login.password):
                request.session['enroll_id'] = enroll_id
                return render(request, 'OnlineFeeSystem/success.html')
            else:
                return render(request, 'OnlineFeeSystem/login.html',
                              {'error': form.add_error('password', 'password is invalid'), 'form': form})
        else:
            return render(request, 'OnlineFeeSystem/login.html')
    else:
        form = Login_form()
        return render(request, 'OnlineFeeSystem/login.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request):
    try:
        token = request.GET.get('q')
        enroll_id = request.GET.get('enroll')
        print token
        print enroll_id
        student = StudentInfo.objects.get(enroll_id=enroll_id)
    except (TypeError, ValueError, OverflowError, student.DoesNotExist):
        student = None

    if student is not None and account_activation_token.check_token(student, token):
        student.email_confirmed = True
        student.token = ''
        student.save()
        # login(request, user)
        return redirect('student_login')
    else:
        return render(request, 'account_activation_invalid.html')


def forgot_password(request):
    if request.method == "GET":
        forgot_pass_form = Forgot_Password()
        return render(request, 'OnlineFeeSystem/forgot.html', {'forgot_form' : forgot_pass_form})
    elif request.method == 'POST':
        forgot_form = Forgot_Password(request.POST)
        if forgot_form.is_valid():
            enroll_id = forgot_form.cleaned_data['enroll_id']
            student = StudentInfo.objects.get(enroll_id = enroll_id)
            if student is not None:
                student.token = account_activation_token.make_token(student)
                print student.token
                student.save()
                # Mail function copied
                message = render_to_string('OnlineFeeSystem/reset_password.html', {
                    'domain': str(get_current_site(request)),
                    'student': student.student_name,
                    'your_enrollment_id': student.enroll_id,
                    'token': account_activation_token.make_token(student)
                })
                to_email = student.email
                email = EmailMessage(subject='Reset your password', body=message, to=[to_email])
                email.send()
                return HttpResponse('Mail sent successfully')
                # End of mail
            else:
                return render(request, 'OnlineFeeSystem/forgot.html',{'forgot_form' : forgot_form, 'error': forgot_form.add_error('enroll_id', 'Invalid enrollment ID')})
        else:
            return HttpResponse('Form is not valid')


def reset_password(request):
    token = request.GET.get('q')
    enroll_id = request.GET.get('enroll')
    student = StudentInfo.objects.filter(token=token, enroll_id = enroll_id)
    if student is not None:
        if request.method == "POST":
            form = reset_password_form(request.POST)
            if form.is_valid():
                password = make_password(request.POST['password'])
                student = StudentInfo.objects.get(enroll_id=enroll_id)
                student.password = password
                student.save()
                return render(request, 'OnlineFeeSystem/reset_password_form.html')
            else:
                return  HttpResponse("Plese change password correctly")
        else:
            form = reset_password_form()
            return render(request, 'OnlineFeeSystem/reset_password_form.html', {'form': form})

    else:
        return HttpResponse('Student is not in our system')




