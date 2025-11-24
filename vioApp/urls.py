from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("emergency/", views.emergency, name="emergency"),
    path("report_incident/", views.report_incident, name="incident"),
    path("incident_history/", views.incident_history, name="incident_history"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("resources", views.resources, name="resources"),
    path("password_reset/", views.password_reset, name="password_reset"),



]