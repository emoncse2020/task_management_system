from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from tasks.forms import TaskModelForm, TaskDetailModelForm
from tasks.models import Employee, Task
from django.db.models import Count, Q

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def manager_dashboard(request):

    
    # print(type)

    

    #getting task count
    # total_task = tasks.count()
    # completed_task = Task.objects.filter(status = "COMPLETED").count()
    # in_progress = Task.objects.filter(status="IN_PROGRESS").count()
    # pending_task = Task.objects.filter(status="PENDING").count()
    type = request.GET.get('type', 'all')


    
    counts = Task.objects.aggregate(
        total = Count('id'),
        completed = Count('id', filter=Q(status="COMPLETED")),
        in_progress = Count('id', filter=Q(status = "IN_PROGRESS")),
        pending = Count('id', filter=Q(status = "PENDING"))
        
        )
    
    base_query = Task.objects.select_related('details').prefetch_related('assigned_to')
    
    #Retriving task data
    if type == 'completed':
        tasks = base_query.filter(status = "COMPLETED")
    elif type == 'in-progress':
        tasks = base_query.filter(status = "IN_PROGRESS")
    elif type == 'pending':
        tasks = base_query.filter(status = "PENDING")
    elif type == 'all':
        tasks = base_query.all()

    context = {
        "tasks":tasks,
        "counts":counts
    }

    return render(request, 'dashboard/manager-dashboard.html', context)



def create_task(request):
    # employees = Employee.objects.all()
    #for get operation
    task_form = TaskModelForm() 
    task_detail_form = TaskDetailModelForm()

    #for post
    if request.method == "POST":
        task_form = TaskModelForm(request.POST) 
        task_detail_form = TaskDetailModelForm(request.POST) 
        if task_form.is_valid() and task_detail_form.is_valid():
            '''For model form data'''
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request,"Task Created Successfully.")
            return redirect('create-task')
    

    context = {
        "task_form":task_form,
        "task_detail_form":task_detail_form
    }
    return render(request, 'task-form.html', context)

def update_task(request, id):
    task = Task.objects.get(id = id)
    # employees = Employee.objects.all()
    #for get operation
    task_form = TaskModelForm(instance = task)
    if task.details:
        task_detail_form = TaskDetailModelForm(instance = task.details)

    #for post
    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance = task) 
        task_detail_form = TaskDetailModelForm(request.POST, instance = task.details) 
        if task_form.is_valid() and task_detail_form.is_valid():
            '''For model form data'''
            
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()
            messages.success(request,"Task Updated Successfully.")
            return redirect('update-task', id)
    

    context = {
        "task_form":task_form,
        "task_detail_form":task_detail_form
    }
    return render(request, 'task-form.html', context)

def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('manager-dashboard')
    else:
        messages.error(request, 'Something went wrong')
        return redirect ('manager-dashboard', )


def view_task(request):
    #retrive all data from task model
    tasks = Task.objects.all()
    #retrive a specific tasks

    task_3 = Task.objects.get(id = 3)
    return render(request, 'show-task.html', {"tasks":tasks, "task_3":task_3})
