from django.contrib import admin
from .models import *

class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "kcalPer100g", "get_kJPer100g", "proteinPer100g", "carbsPer100g", "fatPer100g", "fiberPer100g", "grams_per_teaspoon", "grams_per_tablespoon", "grams_per_piece"]

class MealAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "get_weight", "get_kcal", "get_protein", "get_carbs", "get_fat", "get_fiber"]

class WeightedFoodAdmin(admin.ModelAdmin):
    list_display = ["id", "parentFood", "weight", "get_weight_in_grams", "get_kcal", "get_protein", "get_carbs", "get_fat", "get_fiber", "measurement_type"]

class FoodInMealAdmin(admin.ModelAdmin):
    list_display = ["meal", "food", "food_weight"]

class CountedMealAdmin(admin.ModelAdmin):
    list_display = ["id", "parentMeal", "count"]

class FoodAndMealAdmin(admin.ModelAdmin):
    list_display = ["id", "get_name", "type", "food", "meal"]

admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
admin.site.register(WeightedFood, WeightedFoodAdmin)
admin.site.register(FoodInMeal, FoodInMealAdmin)
admin.site.register(CountedMeal, CountedMealAdmin)
admin.site.register(FoodAndMeal, FoodAndMealAdmin)