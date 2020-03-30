"""project_fitness URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fitness import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('register/',views.signup, name='registration'),
    path('home/',views.home, name='home'),
    path('login/',views.signin, name='login'),
    path('logout/',views.logout_request, name='login'),
    path('bmi/',views.bmi, name='bmi'),
    path('diet/<gender>/<fitness_plan>',views.get_meal_list, name='get_meal_list'),
    path('excercise/<gender>/<fitness_plan>',views.select_excercise_level, name='select_excercise'),
    path('excercise/<gender>/<fitness_plan>/<fitness_level>/',views.get_excercise_list, name='get_excercise_list'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
