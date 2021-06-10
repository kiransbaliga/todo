from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TodoListItem
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
def index(request):
    return render(request,"index.html")    
def todoappView(request):
    all_todo=TodoListItem.objects.filter(todo=True,doing=False,done=False )
    all_doing=TodoListItem.objects.filter(doing=True,done=False,todo=False)
    all_done=TodoListItem.objects.filter(done=True,doing=False,todo=False)
    return render(request,'todolist.html',{'todo':all_todo,'doing':all_doing,'done':all_done})

def addTodoView(request):
    x= request.POST['content']
    new_item=TodoListItem(content=x)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')

def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todoapp/') 

def changetotodo(request,i):
    y=TodoListItem.objects.get(id=i)
    y.doing=False
    y.done=False
    y.todo=True
    y.save()
    print("Todo is working")
    return HttpResponseRedirect('/todoapp/')

def changetodoing(request,i):
    y=TodoListItem.objects.get(id=i)
    y.doing=True
    y.done=False
    y.todo=False
    y.save()
    print("Doing is working")
    return HttpResponseRedirect('/todoapp/')

def changetodone(request,i):
    y=TodoListItem.objects.get(id=i)
    y.doing=False
    y.done=True
    y.todo=False
    y.save()
    print("Done is working")
    return HttpResponseRedirect('/todoapp/')   

def signupView(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.success(request,'User Registered')
            return dashboard(request)
        # else:
        #     form=
    else:
        form=UserCreationForm()
    return render(request,'signup.html',{'form':form})

def signinView(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect(request,'db.html')
    else:
        form =AuthenticationForm()
    return render(request,'signin.html',{'form':form})

def dashboard(request):
    us=request.user
    return render(request,'db.html',{'user':us})