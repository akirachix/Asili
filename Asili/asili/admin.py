from django.contrib import admin
from.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("unique_identifier", "delivered_on")
    search_fields = ("unique_identifier", "delivered_on")

admin.site.register(Notification, NotificationAdmin)