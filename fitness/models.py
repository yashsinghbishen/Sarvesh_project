from django.db import models
# Create your models here.


class Goal(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Meal(models.Model):
    name = models.CharField(max_length=255)
    # goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Food(models.Model):
    name = models.CharField(max_length=255)
    calories = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name
    

class FoodMealGoal(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.goal.name} {self.meal.name} {self.food.name}'
    

class BodyPart(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Equipment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Excercise(models.Model):
    name = models.CharField(max_length=255)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class BodyPartExcercise(models.Model):
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    excercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.excercise.name} for {self.body_part.name}'
    