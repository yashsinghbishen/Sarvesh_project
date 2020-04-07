from django import template
from fitness.models import *

register = template.Library()


@register.inclusion_tag('excercise_header.html')
def load_excercises():
    data = {
        'genders' : list(dict(Gender.options).values()),
        'fitness_plans' : list(dict(FitnessPlan.options).values()),
        'fitness_levels' : list(dict(FitnessLevel.options).values()),
    }
    print(data)
    return data

@register.inclusion_tag('diet_header.html')
def load_diet():
    data = {
        'genders' : list(dict(Gender.options).values()),
        'fitness_plans' : list(dict(FitnessPlan.options).values()),
    }
    return data
