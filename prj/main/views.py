from django.shortcuts import render
from .models import *

def foods(request):
  foods = Food.objects.all()
  context = {
    'foods': foods,
  }
  return render(request, "main/seznam-potravin.html", context)