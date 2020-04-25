from django.db import models
from datetime import datetime

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    duedate = models.DateField(default=datetime.now, blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.title