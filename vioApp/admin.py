from django.contrib import admin
from .models import Incident


admin.site.site_header = "Voice It Out Admin"
admin.site.site_title = "Vio Admin Portal"
admin.site.index_title = "Welcome to the Safety Command Center"

class IncidentAdmin(admin.ModelAdmin):
    list_display = ('incident_type', 'urgency_colored', 'status', 'date_reported', 'user')
    list_filter = ('urgency_level', 'status', 'incident_type')
    search_fields = ('description', 'incident_type')
    readonly_fields = ('urgency_level', 'sentiment_score')

    def urgency_colored(self, obj):
        from django.utils.html import format_html
        color = "green"
        if "Critical" in obj.urgency_level:
            color = "red"
        elif "High" in obj.urgency_level:
            color = "orange"
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>', color, obj.urgency_level)

    urgency_colored.short_description = "AI Risk Assessment"


admin.site.register(Incident, IncidentAdmin)