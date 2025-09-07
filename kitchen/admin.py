from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook, DishType, Dish, Ingredient


@admin.register(Cook)
class CookAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Kitchen fields", {"fields": ("years_of_experience",)}),
    )
    list_display = ("username", "email", "years_of_experience",
                    "is_staff", "is_superuser")


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price")
    list_filter = ("dish_type",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name",)
