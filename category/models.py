from django.db import models
from task.models import TaskModel
# Create your models here.
class TaskCategory(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)
    tasks = models.ManyToManyField(TaskModel, blank= True)

    def __str__(self):
        return self.categoryName