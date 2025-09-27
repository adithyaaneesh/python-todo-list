from datetime import date
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Todo

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        today = date.today()
        if due_date and date.fromisoformat(due_date) < date.today():
            return render(request, 'add_task.html', {
                'error': 'Due date cannot be in the past',
                'today': today
            })
        if title and description:
            Todo.objects.create(
                title =title,
                description = description,
                created_at = timezone.now(),
                due_date = due_date if due_date else None
            )
            return redirect('home')
    return render(request,'add_task.html')

def task_list(request):
    tasks = Todo.objects.all().order_by("-created_at")
    today = date.today()
    pending_task = Todo.objects.all().filter(complete_task = False).count()
    return render(request,'home.html',{'tasks':tasks, 'today':today,'pending_task':pending_task })

def complete_task(request,task_id):
    task = get_object_or_404(Todo,id=task_id)
    task.complete_task = True
    task.save()
    return redirect('home')

def update_task(request,task_id):
    task = get_object_or_404(Todo,id=task_id)

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        today = date.today()
        if due_date and date.fromisoformat(due_date) < date.today():
            return render(request, 'update_task.html', {
                'error': 'Due date cannot be in the past',
                'today': today
            })
        if title and description:
            task.title =title
            task.description = description
            task.due_date = due_date if due_date else None
            task.complete_task = "status" in request.POST 
            task.save()
            return redirect('home')
    return render(request,'update_task.html',{'task':task})

def delete_task(request,task_id):
    task = get_object_or_404(Todo,id=task_id)
    task.delete()
    return redirect('home')




