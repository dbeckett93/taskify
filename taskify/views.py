from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task, Category, Comment
from .forms import TaskForm, CommentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def task_list(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    priority = request.GET.get('priority')
    completed = request.GET.get('completed')

    tasks = Task.objects.all()

    if query:
        tasks = tasks.filter(title__icontains=query)
    if category:
        tasks = tasks.filter(category__name=category)
    if priority:
        tasks = tasks.filter(priority=priority)
    if completed:
        tasks = tasks.filter(completed=completed == 'true')

    return render(request, 'taskify/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'taskify/task_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'taskify/task_detail.html', {'task': task})

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'taskify/task_form.html', {'form': form})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')

@login_required
def task_toggle_completion(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return JsonResponse({'completed': task.completed})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'taskify/register.html', {'form': form})