from django.db import models

class TodoListItem(models.Model):
    content = models.TextField()
    todo=models.BooleanField(default=True)
    doing=models.BooleanField(default=False)
    done=models.BooleanField(default=False)
