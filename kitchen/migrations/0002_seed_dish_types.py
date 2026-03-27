from django.db import migrations


def seed_dish_types(apps, schema_editor):
    DishType = apps.get_model("kitchen", "DishType")
    for name in ["Soup", "Main course", "Dessert", "Salad", "Drink"]:
        DishType.objects.get_or_create(name=name)


def unseed_dish_types(apps, schema_editor):
    DishType = apps.get_model("kitchen", "DishType")
    DishType.objects.filter(
        name__in=["Soup", "Main course", "Dessert", "Salad", "Drink"]
    ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_dish_types, unseed_dish_types),
    ]
