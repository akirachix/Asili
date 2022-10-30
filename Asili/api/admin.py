from django.contrib import admin
from .models import Categories, Designer, User, Kids, Men, Women
 
# Register your models here.
class UserAdmin(admin.ModelAdmin):
   list_display = ("first_name", "last_name", "email", "password")
   search_fields = ("first_name", "last_name", "email", "password")
admin.site.register(User, UserAdmin)
 
class DesignerAdmin(admin.ModelAdmin):
   list_display = ("first_name", "last_name", "email", "password")
   search_fields = ("first_name", "last_name", "email", "password")
admin.site.register(Designer, DesignerAdmin)
 
class CategoriesAdmin(admin.ModelAdmin):
   list_display = ("image", "type",  )
   search_fields = ("image", "type",)
admin.site.register(Categories, CategoriesAdmin)
 
class MenAdmin(admin.ModelAdmin):
   list_display = ("image", "type",)
   search_fields = ("image", "type",)
admin.site.register(Men, MenAdmin)
 
class WomenAdmin(admin.ModelAdmin):
    list_display = ("image", "type",)
    search_fields = ("image", "type", )
admin.site.register(Women, WomenAdmin)
 
class KidsAdmin(admin.ModelAdmin):
    list_display = ("image", "type",)
    search_fields = ("image", "type", )
admin.site.register(Kids, KidsAdmin)
