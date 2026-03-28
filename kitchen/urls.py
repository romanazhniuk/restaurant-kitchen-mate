from django.urls import path
from . import views

app_name = "kitchen"

urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/register/", views.CookRegisterView.as_view(), name="register"),
    path("accounts/login/", views.KitchenLoginView.as_view(), name="login"),
    path("accounts/logout/", views.KitchenLogoutView.as_view(), name="logout"),
    path("cooks/", views.CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", views.CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", views.CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/update/", views.CookUpdateView.as_view(), name="cook-update"),
    path("cooks/<int:pk>/delete/", views.CookDeleteView.as_view(), name="cook-delete"),

    path("dishes/", views.DishListView.as_view(), name="dish-list"),
    path("dish-types/", views.DishTypeListView.as_view(), name="dish-type-list"),
    path("dishes/<int:pk>/", views.DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", views.DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", views.DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", views.DishDeleteView.as_view(), name="dish-delete"),

    path("dish-types/",
         views.DishTypeListView.as_view(),
         name="dish-type-list"),
    path("dish-types/create/",
         views.DishTypeCreateView.as_view(),
         name="dish-type-create"),
    path("dish-types/<int:pk>/update/",
         views.DishTypeUpdateView.as_view(),
         name="dish-type-update"),
    path("dish-types/<int:pk>/delete/",
         views.DishTypeDeleteView.as_view(),
         name="dish-type-delete"),
]