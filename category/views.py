from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from category.models import TaskCategory
from .forms import TaskCategoryForm

# Create your views here.
@login_required
def add_category(request):
    if request.method == 'POST':
        form = TaskCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')
    else:
        form = TaskCategoryForm()
    return render(request, 'category/add_category.html', {'form': form})