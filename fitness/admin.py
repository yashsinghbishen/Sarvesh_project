from django.contrib import admin
from .models import *

# Register your models here.
class FoodMealGoalAdmin(admin.ModelAdmin):
    list_display = ['goal','meal','food']


class ExcerciseAdmin(admin.ModelAdmin):
    list_display = ['name', 'equipment']


class BodyPartExcerciseAdmin(admin.ModelAdmin):
    list_display = ['body_part','excercise','get_required_equipment']

    def get_required_equipment(self, obj):
        return obj.excercise.equipment.name

    get_required_equipment.short_description = 'Equipment'



admin.site.register(Goal)
admin.site.register(Meal)
admin.site.register(Food)
admin.site.register(FoodMealGoal, FoodMealGoalAdmin)
admin.site.register(BodyPart)
admin.site.register(Equipment)
admin.site.register(Excercise,ExcerciseAdmin)
admin.site.register(BodyPartExcercise, BodyPartExcerciseAdmin)
# admin.site.register()