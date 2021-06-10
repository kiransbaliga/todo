"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from todoapp.views import addTodoView, changetodoing, changetodone, changetotodo, dashboard, deleteTodoView, index, signinView, signupView,todoappView
from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render


urlpatterns = [
    path('',index),
    path('signup/',signupView),
    path('dashboard/',dashboard),
    path('signin/',signinView),
    path('admin/', admin.site.urls),
    path('todoapp/',todoappView),
    path('addTodoItem/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('changeTOTODO/<int:i>/',changetotodo),
    path('changeTODOING/<int:i>/',changetodoing),
    path('changeTODONE/<int:i>/',changetodone)
]
