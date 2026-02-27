from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()
    def __str__(self):
        return self.taskTitle
