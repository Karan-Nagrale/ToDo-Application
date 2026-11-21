from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Task

# add task
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

# mark as done
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

# mark as undone
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

# edit task
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task' : get_task,
        }
        return render(request, 'edit_task.html', context)
    
# delete task
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')