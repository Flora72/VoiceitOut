from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.
def index (request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def emergency(request):
    return render(request,'emergency.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def password_reset(request):
    return render(request,'password_reset.html')

def report_incident(request):
    return render(request, 'report_incident.html')

def resources(request):
    return render(request,'resources.html')

def incident_history(request):
    return render(request,'incident_history.html')

def dashboard(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('index')