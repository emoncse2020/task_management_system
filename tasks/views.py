from django.shortcuts import render
from django.http import HttpResponse

from tasks.forms import TaskForm, TaskModelForm
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
            """For django form data"""
            # data = form.cleaned_data

            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to') #list [1,3]

            # task = Task.objects.create(title = title, description = description, due_date = due_date)
            
            # #assigned employee to task

            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id = emp_id)
            #     task.assigned_to.add(employee)

            
    

    context = {
        "form":form
    }
    return render(request, 'task-form.html', context)

def hello_css(request):
    return render(request, 'dashboard/hello-css.html')
