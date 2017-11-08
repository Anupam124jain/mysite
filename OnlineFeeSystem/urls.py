from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from TeacherStudentFeedback import views as core_views
from OnlineFeeSystem import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^studentregister', views.StudentRegister, name='StudentRegister'),

]
