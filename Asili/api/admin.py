from django.contrib import admin
<<<<<<< HEAD
from.models import Notification, User

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("unique_identifier", "delivered_on")
    search_fields = ("unique_identifier", "delivered_on")

admin.site.register(Notification, NotificationAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")

admin.site.register(User, UserAdmin)
=======

# Register your models here.
>>>>>>> d297cd4ece380dad5da3ff589e42bc0bac507867
