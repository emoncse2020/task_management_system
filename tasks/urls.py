
from django.urls import path
from tasks.views import dashboard, manager_dashboard, create_task, hello_css

urlpatterns = [
    path('dashboard/', dashboard),
    path('manager-dashboard/',manager_dashboard),
    path('create-task/', create_task),
    path('hello/', hello_css)
    
]