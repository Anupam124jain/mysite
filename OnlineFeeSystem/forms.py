from django import forms
from OnlineFeeSystem.models import StudentInfo


class Registration_Form(forms.Form):
    Branch = (
        ('select', 'select'),
        ('1', 'Computer Science'),
        ('2', 'Information Technology'),
        ('3', 'Electrical'),
        ('4', 'Electronic & Communication'),
        ('5', 'Civil'),
        ('6', 'Machanical'),

    )
    Semester = (
        ('select', 'select'),
        ('1', 'I'),
        ('2', 'II'),
        ('3', 'III'),
        ('4', 'IV'),
        ('5', 'V'),
        ('6', 'VI'),
        ('7', 'VII'),
        ('8', 'VIII')

    )
    Student_Type = [('D','DaysCaller'),
               ('H','Hosteler')]
    student_name = forms.CharField(max_length=30, label='Student Name')
    fathers_name = forms.CharField(max_length=30, label='Father Name')
    email = forms.EmailField(max_length=100, label='Email')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password')
    branch = forms.ChoiceField(choices = Branch, label="Branch", initial='',widget=forms.Select(), required=True)
    mobile_no = forms.CharField(label='mobileno.', max_length = 15)
    sem = forms.ChoiceField(choices = Semester, label="Semaster", initial='',widget=forms.Select(), required=True)
    student_type = forms.ChoiceField(choices=Student_Type, widget=forms.RadioSelect(attrs=dict(required=True, max_length=50)),
                               label="Student Type")


class Login_form(forms.Form):
    enroll_id = forms.CharField(max_length=30, label='Enrollment id')
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Password')


class Forgot_Password(forms.Form):
    enroll_id = forms.CharField(max_length=100, label='Enroll ID')

class reset_password_form(forms.Form):
    password = forms.CharField(max_length=50, label='New Password')
    # confirm_password = forms.CharField(max_length=50, label='confirm_password')