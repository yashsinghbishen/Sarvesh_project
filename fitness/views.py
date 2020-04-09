from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
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


@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def goal(request):
    return render(request, 'exericelist.html')   

@login_required(login_url='/login/')
def Nutritiondetails(request):
    return render(request, 'Nutritiondetails.html')      

@login_required(login_url='/login/')
def goal(request):
    return render(request, 'goal1.html')


@login_required(login_url='/login/')
def exericelist(request):
    return render(request, 'exericelist.html')


@login_required(login_url='/login/')
def leanmode(request):
    return render(request, 'leanmode.html')


@login_required(login_url='/login/')
def shreddha(request):
    return render(request, 'shreddha.html')


@login_required(login_url='/login/')
def get_17inches(request):
    return render(request, '17inches.html')


@login_required(login_url='/login/')
def diebetes(request):
    return render(request, 'diebetes.html')


@login_required(login_url='/login/')
def fightcancer(request):
    return render(request, 'fightcancer.html')


@login_required(login_url='/login/')
def logout_request(request):
    logout(request)
    return render(request, 'index.html')


@login_required(login_url='/login/')
def get_meal_list(request, gender, fitness_plan):
    print(gender, fitness_plan)
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
        meal.update({'foods': foods})
        print(meal)
        meal_list.append(meal)
    return render(request, 'show_meals.html', {'meals': meal_list})


@login_required(login_url='/login/')
def select_excercise_level(request, gender, fitness_plan):
    return render(request, 'select_excercise.html', {'gender': gender, 'fitness_plan': fitness_plan})


@login_required(login_url='/login/')
def get_excercise_list(request, gender, fitness_plan, fitness_level):
    print(gender, fitness_plan, fitness_level)
    body_parts = BodyPart.objects.filter(
        pk__in=BodyPartExcercise.objects.filter(
            gender=gender,
            fitness_plan=fitness_plan,
            fitness_level=fitness_level
        ).values('body_part')
    )
    # print(body_parts)
    # body_part_list = []
    # for body_part in body_parts.values():
    #     excercises = BodyPartExcercise.objects.filter(
    #         gender=gender,
    #         fitness_plan=fitness_plan,
    #         fitness_level=fitness_level,
    #         body_part=body_part['id']
    #     )
    #     body_part.update({'excercises':excercises})
    #     print(body_part)
    #     body_part_list.append(body_part)
    return render(request, 'show_excercise.html', {
        'gender': gender,
        'fitness_plan': fitness_plan,
        'fitness_level': fitness_level,
        'body_parts': body_parts
    })


@login_required(login_url='/login/')
def get_excercise_detail(request, gender, fitness_plan, fitness_level, body_part):
    print(gender, fitness_plan, fitness_level)
    body_part = BodyPart.objects.get(pk=body_part)
 
    excercises = BodyPartExcercise.objects.filter(
        gender=gender,
        fitness_plan=fitness_plan,
        fitness_level=fitness_level,
        body_part=body_part
    )
    return render(request, 'show_excercise_detail.html', {
        'gender': gender,
        'fitness_plan': fitness_plan,
        'fitness_level': fitness_level,
        'body_part': body_part,
        'excercises': excercises,
    })



@login_required(login_url='/login/')
def excercise_posts(request, gender):

    excercises = ExcercisePost.objects.filter(
        gender=gender
    )
    return render(request, 'excercise_posts.html', {
        'excercises': excercises,
    })


@login_required(login_url='/login/')
def diet_posts(request, gender):

    diets = FoodPost.objects.filter(
        gender=gender
    )
    return render(request, 'diet_posts.html', {
        'diets': diets,
    })




@login_required(login_url='/login/')
def bmi(request):
    if request.method == "POST":
        form = BmiForm(request.POST)
        if form.is_valid():
            gender = form.cleaned_data["gender"]
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = int(weight/((height*0.305)*(height*0.305)))
            print(gender)
            return render(request, "bmi.html", {"bmi": bmi, "gender": gender})
    else:
        form = BmiForm()
    return render(request, "bmi.html", {"form": form})
