from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from TeacherStudentFeedback import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^TeacherRegister', core_views.TeacherRegister, name='TeacherRegister'),
    url(r'^TeacherLogin', core_views.TeacherLogin, name='TeacherLogin'),
    url(r'^TeacherFeedback', core_views.TeacherFeedback, name='TeacherFeedback'),
]
