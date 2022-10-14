from django.contrib import admin
from.models import Bodytype, Categories, Notification, Customer ,Preference , Bodytype, Categories

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("unique_identifier", "delivered_on")
    search_fields = ("unique_identifier", "delivered_on")

admin.site.register(Notification, NotificationAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "gender", "email",)
    search_fields = ("full_name", "gender", "email",)

admin.site.register(Customer, CustomerAdmin)

class PreferenceAdmin(admin.ModelAdmin):
    list_display = ("measurement", "color", "material",  )
    search_fields = ("measurement", "color", "material", )

admin.site.register(Preference, PreferenceAdmin)

class BodytypeAdmin(admin.ModelAdmin):

    list_display = ("plump", "triangle", "plus_size",)
    search_fields = ("plump", "triangle", "plus_size",)

admin.site.register(Bodytype, BodytypeAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("men", "women", "kids")
    search_fields = ("men", "women", "kids")
admin.site.register(Categories, CategoriesAdmin)

