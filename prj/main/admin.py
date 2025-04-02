from django.contrib import admin
from .models import Food, Meal, WeightedFood, FoodInMeal

class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "kcalPer100g", "proteinPer100g", "carbsPer100g", "fatPer100g", "fiberPer100g"]

class MealAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "get_weight", "get_kcal", "get_protein", "get_carbs", "get_fat", "get_fiber"]

class WeightedFoodAdmin(admin.ModelAdmin):
    list_display = ["id", "parentFood", "weight", "get_kcal", "get_protein", "get_carbs", "get_fat", "get_fiber"]

class FoodInMealAdmin(admin.ModelAdmin):
    list_display = ["meal", "food", "food_weight"]

admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(WeightedFood, WeightedFoodAdmin)
admin.site.register(FoodInMeal, FoodInMealAdmin)