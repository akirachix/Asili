from django.contrib import admin
from.models import  User, Category, Cloth

# class NotificationAdmin(admin.ModelAdmin):
#     list_display = ("unique_identifier", "delivered_on")
#     search_fields = ("unique_identifier", "delivered_on")
# admin.site.register(Notification, NotificationAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")
admin.site.register(User, UserAdmin)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("men", "women","kids")
    search_fields = ("men", "women","kids")
admin.site.register(Category, CategoryAdmin)
class ClothAdmin(admin.ModelAdmin):
    list_display = ("image", "type","gender")
    search_fields = ("image",)
admin.site.register(Cloth, ClothAdmin)
# Register your models here.