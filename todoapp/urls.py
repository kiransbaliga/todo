from django.urls import path
from django.shortcuts import render
from . import views
app_name = "Kanbaan" 
def index(request):
    return render(request,"todoapp/index.html")
urlpatterns=[
    path("",views.index,name="index"),
]