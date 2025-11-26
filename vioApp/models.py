from django.db import models
from django.contrib.auth.models import User


class Incident(models.Model):
    # Link to a user, but allow null=True for anonymous reporting (Crucial for safety apps)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    incident_type = models.CharField(max_length=100)
    description = models.TextField()

    # We will set these automatically using Python logic
    urgency_level = models.CharField(max_length=20, default="Normal")
    sentiment_score = models.FloatField(default=0.0)  # Stores -1.0 (Bad) to 1.0 (Good)

    status = models.CharField(max_length=50, default="Pending")
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_type} ({self.urgency_level}) - {self.date_reported.strftime('%Y-%m-%d')}"