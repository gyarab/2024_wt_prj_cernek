from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=300)
    kcalPer100g = models.IntegerField(null=True, blank=True)
    proteinPer100g = models.IntegerField(null=True, blank=True)
    carbsPer100g = models.IntegerField(null=True, blank=True)
    fatPer100g = models.IntegerField(null=True, blank=True)
    fiberPer100g = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
class WeightedFood(models.Model):
    weight = models.IntegerField(null=True, blank=True)
    parentFood = models.ForeignKey(Food, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.parentFood} {self.weight}"
    
    def get_kcal(self):
        return self.weight * self.parentFood.kcalPer100g
    
class Meal(models.Model):
    name = models.CharField(max_length=400)
    foods = models.ManyToManyField(WeightedFood)

    def __str__(self):
        return f"{self.name}"