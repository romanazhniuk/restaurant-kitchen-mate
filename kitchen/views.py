from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from kitchen.models import Dish, Cook, DishType


def index(request):
    return render(request, "restaurant/index.html")


class DishListView(generic.ListView):
    model = Dish
    context_object_name = "dish_list"
    template_name = "dish_list.html"


class DishTypeListView(ListView):
    model = DishType
    context_object_name = "dishtype_list"
    template_name = "kitchen/dishtype_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "dish_detail.html"


class DishTypeCreateView(CreateView):
    model = DishType
    fields = ["name"]                         # adjust fields to your model
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "kitchen/dishtype_form.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(DeleteView):
    model = DishType
    template_name = "kitchen/dishtype_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    template_name = "dish_form.html"
    success_url = "/dishes/"


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    template_name = "dish_form.html"
    success_url = "/dishes/"


class DishDeleteView(generic.DeleteView):
    model = Dish
    template_name = "dish_confirm_delete.html"
    success_url = "/dishes/"


class CookListView(generic.ListView):
    model = Cook
    context_object_name = "cook_list"
    template_name = "cook_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "cook_detail.html"


class CookCreateView(generic.CreateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "email", "years_of_experience")
    template_name = "cook_form.html"
    success_url = "/cooks/"


class CookUpdateView(generic.UpdateView):
    model = Cook
    fields = ("username", "first_name", "last_name", "email", "years_of_experience")
    template_name = "cook_form.html"
    success_url = "/cooks/"


class CookDeleteView(generic.DeleteView):
    model = Cook
    template_name = "cook_confirm_delete.html"
    success_url = "/cooks/"
