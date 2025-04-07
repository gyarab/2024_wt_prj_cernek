from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=300)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    kcalPer100g = models.IntegerField(null=True, blank=True)
    proteinPer100g = models.FloatField(null=True, blank=True)
    carbsPer100g = models.FloatField(null=True, blank=True)
    fatPer100g = models.FloatField(null=True, blank=True)
    fiberPer100g = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class WeightedFood(models.Model):
    weight = models.IntegerField(null=True, blank=True)
    parentFood = models.ForeignKey(Food, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.parentFood} {self.weight}"
    
    def get_kcal(self):
        return (int)((self.weight/100) * self.parentFood.kcalPer100g)
    
    def get_protein(self):
        return (int)((self.weight/100) * self.parentFood.proteinPer100g)
    
    def get_carbs(self):
        return (int)((self.weight/100) * self.parentFood.carbsPer100g)
    
    def get_fat(self):
        return (int)((self.weight/100) * self.parentFood.fatPer100g)
    
    def get_fiber(self):
        return (int)((self.weight/100) * self.parentFood.fiberPer100g)
    
class Meal(models.Model):
    name = models.CharField(max_length=400)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_weight(self):
        all_relations = FoodInMeal.objects.filter(meal=self)
        total = 0
        for i in all_relations:
            total += i.food_weight
        return total
    
    def get_kcal(self):
        all_relations = FoodInMeal.objects.filter(meal=self)
        total = 0
        for i in all_relations:
            total += (int)((i.food_weight/100) * i.food.kcalPer100g)
        return total
    
    def get_protein(self):
        all_relations = FoodInMeal.objects.filter(meal=self)
        total = 0
        for i in all_relations:
            total += (int)((i.food_weight/100) * i.food.proteinPer100g)
        return total
    
    def get_carbs(self):
        all_relations = FoodInMeal.objects.filter(meal=self)
        total = 0
        for i in all_relations:
            total += (int)((i.food_weight/100) * i.food.carbsPer100g)
        return total
    
    def get_fat(self):
        all_relations = FoodInMeal.objects.filter(meal=self)
        total = 0
        for i in all_relations:
            total += (int)((i.food_weight/100) * i.food.fatPer100g)
        return total
    
    def get_fiber(self):
        all_relations = FoodInMeal.objects.filter(meal=self)
        total = 0
        for i in all_relations:
            total += (int)((i.food_weight/100) * i.food.fiberPer100g)
        return total
        
class CountedMeal(models.Model):
    parentMeal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    count = models.IntegerField(null=True, blank=True)

class FoodInMeal(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_weight = models.IntegerField(null=True, blank=True)