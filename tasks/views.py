from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm


def task_list(request):
    """Display all tasks with status and action buttons."""
    tasks = Task.objects.all()
    total_count = tasks.count()
    completed_count = tasks.filter(completed=True).count()
    pending_count = total_count - completed_count

    context = {
        'tasks': tasks,
        'total_count': total_count,
        'completed_count': completed_count,
        'pending_count': pending_count,
    }
    return render(request, 'tasks/task_list.html', context)


def task_create(request):
    """Create a new task."""
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskCreateForm()

    return render(request, 'tasks/task_form.html', {'form': form, 'action': 'Add'})


def task_update(request, pk):
    """Edit an existing task."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'task': task, 'action': 'Update'})


def task_toggle(request, pk):
    """Toggle completed status of a task."""
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    status_str = "completed" if task.completed else "pending"
    messages.info(request, f'Task marked as {status_str}.')
    return redirect('task_list')


def task_delete(request, pk):
    """Delete a task with confirmation."""
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')

    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
