from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import TodoListItem
from django.shortcuts import render


def todoappView(request):
    all_todo=TodoListItem.objects.filter(todo=True)
    all_doing=TodoListItem.objects.filter(doing=True)
    all_done=TodoListItem.objects.filter(done=True)
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
    return HttpResponseRedirect('/todoapp/')
def changetodoing(request,i):
    y=TodoListItem.objects.get(id=i)
    y.doing=True
    y.done=False
    y.todo=False
    y.save()
    return HttpResponseRedirect('/todoapp/')
def changetodone(request,i):
    y=TodoListItem.objects.get(id=i)
    y.doing=False
    y.done=True
    y.todo=False
    y.save()
    return HttpResponseRedirect('/todoapp/')   