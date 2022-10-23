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
    list_display = ("new", "men", "women", "kids", "mostpopular" )
    search_fields = ("new", "men", "women", "kids", "mostpopular")
admin.site.register(Categories, CategoriesAdmin)

class MenAdmin(admin.ModelAdmin):
    list_display = ("trousers", "shirts", "jackets", "suits")
    search_fields = ("trousers", "shirts", "jackets", "suits")
admin.site.register(Men, MenAdmin)

class WomenAdmin(admin.ModelAdmin):
    list_display = ("trousers", "shirts", "jackets", "dress", "skirts")
    search_fields = ("trousers", "shirts", "jackets", "dress", "skirts")
admin.site.register(Women, WomenAdmin)

class KidsAdmin(admin.ModelAdmin):
    list_display = ("trousers", "shirts", "jackets", "dress", "suits")
    search_fields = ("trousers", "shirts", "jackets", "dress", "suits")
admin.site.register(Kids, KidsAdmin)