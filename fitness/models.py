from django.db import models
# Create your models here.

class Gender:
    female = 'female'
    male = 'male'

    options = [
        (male,male),
        (female, female),
    ]

class Category:
    veg = 'Veg'
    non_veg = 'Non-Veg'

    options = [
        (veg, veg),
        (non_veg, non_veg)
    ]

class FitnessPlan:
    gain = 'gain'
    lose = 'lose'

    options = [
        (gain, gain),
        (lose, lose),
    ]


class FitnessLevel:
    beginer = 'beginer'
    intermediate = 'intermediate'
    advance = 'advance'
    

    options = [
        (beginer, beginer),
        (intermediate,intermediate),
        (advance,advance),
    ]

class Goal(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(choices=Gender.options, max_length=20, default=Gender.male)
    fitness_plan = models.CharField(choices=FitnessPlan.options, max_length=20, default=FitnessPlan.lose)
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
    image = models.ImageField(upload_to='excercises',null=True)

    def __str__(self):
        return self.name
    

class BodyPartExcercise(models.Model):
    gender = models.CharField(choices=Gender.options, max_length=20, default=Gender.male)
    fitness_plan = models.CharField(choices=FitnessPlan.options, max_length=20, default=FitnessPlan.lose)
    fitness_level = models.CharField(choices=FitnessLevel.options, max_length=20, default=FitnessLevel.beginer)
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    excercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    reps = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.excercise.name} for {self.body_part.name}'
    
class ExcercisePost(models.Model):
    gender = models.CharField(choices=Gender.options, max_length=20, default=Gender.male)
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
    excercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='excercises_post',null=True)
    description = models.CharField(max_length=255)
    
class FoodPost(models.Model):
    gender = models.CharField(choices=Gender.options, max_length=20, default=Gender.male)
    category = models.CharField(choices=Category.options, max_length=10, default=Category.veg)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='diet_post',null=True)
    description = models.CharField(max_length=255)