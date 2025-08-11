from django import forms
from .models import Dish, Cook
from django.contrib.auth.forms import UserCreationForm


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("years_of_experience",)
