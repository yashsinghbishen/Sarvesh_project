from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def logout_request(request):
    logout(request)
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'rigisteration.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SingInForm()
    return render(request, 'login.html', {'form': form})

def get_meal_list(request,gender,fitness_plan):
    print(gender,fitness_plan)
    meals = Meal.objects.filter(
        pk__in=FoodMealGoal.objects.filter(
            goal__gender=gender,
            goal__fitness_plan=fitness_plan
        ).values('meal')
    )
    print(meals)
    meal_list = []
    for meal in meals.values():
        foods = Food.objects.filter(
            pk__in=FoodMealGoal.objects.filter(
                goal__gender=gender,
                goal__fitness_plan=fitness_plan,
                meal__id=meal['id']
            ).values('food')
        )
        meal.update({'foods':foods})
        print(meal)
        meal_list.append(meal)
    return render(request,'show_meals.html', {'meals':meal_list})

    

def get_excercise_list(request,gender,fitness_plan, fitness_level):
    print(gender,fitness_plan, fitness_level)
    body_parts = BodyPart.objects.filter(
        pk__in=BodyPartExcercise.objects.filter(
            gender=gender,
            fitness_plan=fitness_plan,
            fitness_level=fitness_level
        ).values('body_part')
    )
    print(body_parts)
    body_part_list = []
    for body_part in body_parts.values():
        excercises = BodyPartExcercise.objects.filter(
            gender=gender,
            fitness_plan=fitness_plan,
            fitness_level=fitness_level,
            body_part=body_part['id']
        )
        body_part.update({'excercises':excercises})
        print(body_part)
        body_part_list.append(body_part)
    return render(request,'show_excercise.html', {'body_parts':body_part_list})



def bmi(request):
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = weight/height*2
            return render(request, "bmi.html", {"form": form, "bmi": bmi})
    else:
        form = BmiForm()
    return render(request, "bmi.html", {"form": form})
