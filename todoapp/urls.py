from django.urls import path
from django.shortcuts import render
from . import views
app_name = "Kanbaan" 


urlpatterns=[
    path("",views.index,name="index"),
]