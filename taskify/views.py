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

    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.task = task
            comment.save()
            return redirect('task_detail', pk=task.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'task_detail.html', {'task': task, 'comments': comments, 'comment_form': comment_form})

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
    return render(request, 'task_form.html', {'form': form})

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
    return render(request, 'register.html', {'form': form})