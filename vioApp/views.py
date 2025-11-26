from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Incident
from textblob import TextBlob
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


# --- Public Pages & Data Handlers ---

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def emergency(request):
    return render(request, 'emergency.html')


def resources(request):
    return render(request, 'resources.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # In a real app, we would send an email here.
        # For the Hackathon, we simulate it with a success message.
        messages.success(request, f"Thank you, {name}. Your message has been sent to our team.")
        return redirect('contact')
    return render(request, 'contact.html')


# --- AUTHENTICATION VIEWS ---

def signup(request):
    if request.method == 'POST':
        # 1. Get data
        username = request.POST['username']
        email = request.POST.get('email')
        password = request.POST['password']

        # 2. Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken! Please choose another.")
            return redirect('signup')

        # 3. Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # 4. Success
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


def password_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        messages.info(request, f"A password reset link has been sent to {email}.")
        return redirect('login')
    return render(request, 'password_reset.html')


def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('index')

@login_required(login_url='login')
def report_incident(request):
    if request.method == 'POST':
        inc_type = request.POST.get('incident_type')
        desc = request.POST.get('description')

        # 1. AI Analysis
        analysis = TextBlob(desc)
        score = analysis.sentiment.polarity

        # 2. Urgency Logic
        trigger_words = ['suicide', 'kill', 'hurt', 'danger', 'blood', 'immediately']
        is_urgent = any(word in desc.lower() for word in trigger_words)

        if is_urgent or score < -0.5:
            urgency = "Critical 🔴"
        elif score < 0:
            urgency = "High 🟠"
        else:
            urgency = "Normal 🟢"

        # 3. Save Data
        new_incident = Incident(
            incident_type=inc_type,
            description=desc,
            urgency_level=urgency,
            sentiment_score=score,
            user=request.user
        )
        new_incident.save()

        messages.success(request, "Report submitted safely. Logic analysis complete.")
        return redirect('dashboard')

    return render(request, 'report_incident.html')


@login_required(login_url='login')
def dashboard(request):
    user_incidents = Incident.objects.filter(user=request.user).order_by('-date_reported')
    return render(request, 'dashboard.html', {'incidents': user_incidents})


@login_required(login_url='login')
def incident_history(request):
    user_incidents = Incident.objects.filter(user=request.user).order_by('-date_reported')
    return render(request, 'incident_history.html', {'incidents': user_incidents})