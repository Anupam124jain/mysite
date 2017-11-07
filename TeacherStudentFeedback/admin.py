from django.contrib import admin
from .models import Student,Teacher,student_teacher

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(student_teacher)
class student_teacherAdmin(admin.ModelAdmin):
    pass
