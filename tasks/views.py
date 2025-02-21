from django.shortcuts import render
from django.http import HttpResponse

from tasks.forms import TaskModelForm
from tasks.models import Employee, Task

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')

def create_task(request):
    # employees = Employee.objects.all()

    form = TaskModelForm() #for get

    if request.method == "POST":
        form = TaskModelForm(request.POST, ) #for post
        if form.is_valid():
            '''For model form data'''
            form.save()
            return render(request, 'task-form.html', {"form":form , "message" :"Task added successfully"})
    

    context = {
        "form":form
    }
    return render(request, 'task-form.html', context)

def view_task(request):
    #retrive all data from task model
    tasks = Task.objects.all()
    #retrive a specific tasks

    task_3 = Task.objects.get(id = 3)
    return render(request, 'show-task.html', {"tasks":tasks, "task_3":task_3})
