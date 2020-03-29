from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class SingInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class BmiForm(forms.Form):
    # name = forms.CharField(required=False)
    gender = forms.ChoiceField(choices=Gender.options, widget=forms.RadioSelect(), required=True)
    height = forms.FloatField(label="Height in meters:", required=True, min_value=0)
    weight = forms.FloatField(label="Weight in kg:", required=True, min_value=0)
