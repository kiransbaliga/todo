from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class TodoListItem(models.Model):
    content = models.TextField()
    todo=models.BooleanField(default=True)
    doing=models.BooleanField(default=False)
    done=models.BooleanField(default=False)

class project(models.Model):
    pname=models.TextField()
    toboard = models.ForeignKey(TodoListItem,on_delete=models.CASCADE)
    createdby= models.ForeignKey(User,on_delete=models.CASCADE)

    