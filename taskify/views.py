from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'taskify/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskify/task_form.html', {'form': form})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskify/task_detail.html', {'task': task})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskify/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

def task_toggle_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed}) 