from django.contrib import admin
from django.urls import path
from django.contrib.auth import logout
from .views import login_user,signup,home,logout_user

urlpatterns = [
    path('login/',login_user),
    path('signup/',signup),
    path('home/',home),
    path('logout/',logout_user),
    
    
]