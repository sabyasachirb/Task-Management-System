from django.shortcuts import render, redirect, get_object_or_404

import task
from .models import TaskModel
from category.models import TaskCategory
from .forms import TaskModelForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def show_tasks(request):    
    tasks = TaskModel.objects.all()
    return render(request, 'task/show_tasks.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task = form.save()
            selected_catagories = form.cleaned_data['taskCategory']
            for catagory in selected_catagories:
                catagory.tasks.add(task)
            return redirect('show_my_tasks')
    else:
        form = TaskModelForm()
    return render(request, 'task/add_task.html', {'form': form})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    if request.method == 'POST':
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            task.taskcategory_set.set(form.cleaned_data['taskCategory'])
            return redirect('show_my_tasks')
    else:
        form = TaskModelForm(instance=task)
    return render(request, 'task/edit_task.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    task.delete()
    return redirect('show_my_tasks')

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('show_my_tasks')


@login_required
def show_my_tasks(request):
    tasks = TaskModel.objects.filter(user=request.user, is_completed=False)
    return render(request, 'task/show_my_tasks.html', {'tasks': tasks})
