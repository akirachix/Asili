from django.contrib import admin
from.models import Notification, User, Category, Cloth

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("unique_identifier", "delivered_on")
    search_fields = ("unique_identifier", "delivered_on")

admin.site.register(Notification, NotificationAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")

admin.site.register(User, UserAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("men", "men")
    search_fields = ("men", "men")

admin.site.register(Category, CategoryAdmin)

class ClothAdmin(admin.ModelAdmin):
    list_display = ("image", "image")
    search_fields = ("image", "image")

admin.site.register(Cloth, ClothAdmin)