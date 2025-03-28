from django.contrib import admin
from .models import Food, Meal, WeightedFood

class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "kcalPer100g", "proteinPer100g", "carbsPer100g", "fatPer100g", "fiberPer100g"]

class MealAdmin(admin.ModelAdmin):
    list_display = ["name"]

class WeightedFoodAdmin(admin.ModelAdmin):
    list_display = ["id", "weight", "get_kcal"]

admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(WeightedFood, WeightedFoodAdmin)