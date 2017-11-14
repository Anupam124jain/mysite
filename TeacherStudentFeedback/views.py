# from django.contrib.auth import login, authenticate
from TeacherStudentFeedback.forms import TeacherFeedbackForm,TeacherSignupForm, TeacherLoginForm
from  TeacherStudentFeedback.models import Student,Teacher
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render


def TeacherRegister(request):
    if request.method == 'POST':
        form =  TeacherSignupForm(request.POST)
        if form.is_valid():
            password = make_password(request.POST['password'])
            teacher_register = Teacher(teacher_id = request.POST['teacher_id'],
                                       teacher_name = request.POST['teacher_name'],
                                       password = password
                                       )
            teacher_register.save()

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

            return render(request, 'success.html')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = TeacherLoginForm()
        return render(request, 'login.html', {'form': form})


def TeacherFeedback(request):
    if request.method == 'POST':
        form = TeacherFeedbackForm(request.POST)
        if form.is_valid():
            student = Student.objects.get(id=request.POST['student_name'])
            student.student_rating = request.POST['student_rating']
            student.student_remarks = request.POST['student_remarks']
            return render(request, 'success.html')
        else:
            return render(request, 'login.html')

    else:
        form = TeacherFeedbackForm()
        return render(request, 'feedback.html', {'form':form})


