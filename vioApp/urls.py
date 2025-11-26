from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('resources/', views.resources, name='resources'),  # Fixed missing slash

    # The Core Features (Top 3 Worthy)
    path('emergency/', views.emergency, name='emergency'),

    # We use the same URL for showing the form AND submitting it (Professional Standard)
    path('report/', views.report_incident, name='report_incident'),

    # Auth System
    path('login/', views.login_view, name='login'),  # FIXED: Points to login_view, not login
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),

    # User Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.incident_history, name='incident_history'),
]