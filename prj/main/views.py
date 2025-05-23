from django.shortcuts import render
from .models import *

def foods(request):
  foods = FoodAndMeal.objects.all()
  search = request.GET.get('search')
  
  if search:
    newFoods = []
    for food in foods:
      if search.lower() in food.get_name().lower():
        newFoods.append(food)
    foods = newFoods
        

  context = {
    "foods": foods,
  }
  return render(request, "main/seznam-potravin.html", context)

def food_detail(request, food_id):
    item = FoodAndMeal.objects.get(id=food_id)
    if item.type == "food":
        food = Food.objects.get(id=item.food.id)
        return render(request, 'main/detail-potraviny.html', {'food': food})
    elif item.type == "meal":
        meal = Meal.objects.get(id=item.meal.id)
        return render(request, 'main/detail-jidla.html', {'meal': meal})

def weighted_foods(request):
  weighted_foods = WeightedFood.objects.all()
  context = {
    "weighted_foods" : weighted_foods,
  }
  return render(request, "main/seznam-potravin-v-souctu.html", context)

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