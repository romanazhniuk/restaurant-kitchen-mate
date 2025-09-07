from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.username} ({self.years_of_experience} yrs)"


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    # refer to the swappable user model (which will be kitchen.Cook)
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes", blank=True)

    def __str__(self) -> str:
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    dishes = models.ManyToManyField(Dish, related_name="ingredients", blank=True)

    def __str__(self) -> str:
        return self.name
