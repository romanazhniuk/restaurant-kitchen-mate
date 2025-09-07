from django.contrib import admin
from .models import DishType, Cook, Dish, Ingredient
from django.contrib.auth.admin import UserAdmin


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Kitchen fields", {"fields": ("years_of_experience",)}),
    )
    list_display = ("username", "email", "years_of_experience", "is_staff", "is_superuser")


admin.site.register(DishType)
admin.site.register(Cook)
admin.site.register(Dish)
admin.site.register(Ingredient)
