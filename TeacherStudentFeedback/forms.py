from django import forms
from TeacherStudentFeedback.models import Student,Teacher
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

class TeacherFeedbackForm(forms.Form):
    Student_Ratings = (
        ('select', 'select'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    student_name = forms.ModelChoiceField(queryset=Student.objects.all().order_by('student_name'))
    student_rating = forms.ChoiceField(choices = Student_Ratings , label="Student Rating", initial='', widget=forms.Select(), required=True)
    student_remarks = forms.CharField(max_length=50, label='Student Remarks',required=False)

class TeacherSignupForm(forms.Form):
    teacher_id = forms.CharField(max_length=30, label='Teacher Id')
    teacher_name = forms.CharField(max_length=30, label='Teacher Name')
    password = forms.CharField(max_length=30, label='Password')

class TeacherLoginForm(forms.Form):
    teacher_id = forms.ModelChoiceField(queryset=Teacher.objects.all().order_by('teacher_id'), label='teacher_id')
    password = forms.CharField(max_length=30, label='Password')
