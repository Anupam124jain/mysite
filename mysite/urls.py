
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'', include('TeacherStudentFeedback.urls')),
    url(r'', include('OnlineFeeSystem.urls')),
]
