from django.db import models

class Incident(models.Model):
    incident_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50, default="Pending")
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_type} - {self.status}"
