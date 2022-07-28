from django.contrib import admin
from django.urls import path,include
from .views import allblogs,readblog,addblog,savenewblog

urlpatterns = [
     path('allblogs/',allblogs),
     path('read/<int:id>/',readblog),
     path('addblog/', addblog),
     path('savenewblog/',savenewblog)
]