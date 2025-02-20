from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

def manager_dashboard(request):
    return render(request, 'dashboard/manager-dashboard.html')
