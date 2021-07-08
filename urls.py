from django.contrib import admin
from django.urls import path
from Jigsapp import views

urlpatterns = [
    path('insert', views.index, name='Home'),
    path('', views.showData, name='Show'),
    path('login', views.loginData, name='Login'),
   
]