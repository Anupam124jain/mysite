from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from OnlineFeeSystem.views import *

urlpatterns = [
    url(r'^studentregister', student_register, name='student_register'),
    url(r'^studentlogin', student_login, name='student_login'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/', activate, name='activate'),
    url(r'^forgotpass/', forgot_password, name='forgot_password'),
    url(r'^reset-password/', reset_password, name='reset_password'),
   ]


