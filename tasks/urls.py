
from django.urls import path
from tasks.views import dashboard, manager_dashboard, create_task, view_task

urlpatterns = [
    path('dashboard/', dashboard),
    path('manager-dashboard/',manager_dashboard),
    path('create-task/', create_task),
    path('view-task/', view_task)
    
    
]