from django.db import models


class Student(models.Model):

    student_id = models.CharField(max_length=30,unique=True)
    student_name = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    student_rating = models.IntegerField(null=True)
    student_remarks = models.CharField(max_length=50)


    def __str__(self):
        return self.student_name

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=30, unique=True)
    teacher_name = models.CharField(max_length=30)
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.teacher_name

class student_teacher(models.Model):
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(Teacher)

    def __str__(self):
        return self.student_id

