from django.shortcuts import render
from .models import *

def foods(request):
  foods = Food.objects.all()
  meals = Meal.objects.all()
  context = {
    "foods": foods,
  }
  return render(request, "main/seznam-potravin.html", context)

def food_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    return render(request, 'main/detail-potraviny.html', {'food': food})

def weighted_foods(request):
  weighted_foods = WeightedFood.objects.all()
  context = {
    "weighted_foods" : weighted_foods,
  }
  return render(request, "main/seznam-potravin-v-souctu.html", context)

def meals(request):
  meals = Meal.objects.all()
  context = {
    "meals" : meals,
  }
  return render(request, "main/seznam-jidel.html", context)

def homepage(request):
  weighted_foods = WeightedFood.objects.all()
  counted_meals = CountedMeal.objects.all()
  totalKcal = 0
  totalProtein = 0
  totalCarbs = 0
  totalFat = 0
  totalFiber = 0

  for food in weighted_foods:
    totalKcal += food.get_kcal()
    totalProtein += food.get_protein()
    totalCarbs += food.get_carbs()
    totalFat += food.get_fat()
    totalFiber += food.get_fiber()

  for meal in counted_meals:
    totalKcal += meal.parentMeal.get_kcal() * meal.count
    totalProtein += meal.parentMeal.get_protein() * meal.count
    totalCarbs += meal.parentMeal.get_carbs() * meal.count
    totalFat += meal.parentMeal.get_fat() * meal.count
    totalFiber += meal.parentMeal.get_fiber() * meal.count

  totalkJ = round(totalKcal * 4.185)

  context = {
    "totalKcal": totalKcal,
    "totalkJ": totalkJ,
    "totalProtein": totalProtein,
    "totalCarbs": totalCarbs,
    "totalFat": totalFat,
    "totalFiber": totalFiber,
  }
  return render(request, "main/homepage.html", context)