
from django.urls import path
from tasks.views import dashboard, manager_dashboard

urlpatterns = [
    path('dashboard/', dashboard),
    path('manager-dashboard/',manager_dashboard)
    
]