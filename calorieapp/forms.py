from django import forms
from django.contrib.auth.forms import UserCreationForm

from calorieapp.models import Login, userlogin, Food, Meal, workout


class DateInput(forms.DateInput):
    input_type = "date"

class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput,label = 'password')
    password2 = forms.CharField(widget = forms.PasswordInput, label = 'Confirm password')
    class Meta:
        model = Login
        fields = ('username','password1','password2')

class userloginform(forms.ModelForm):
    class Meta:
        model = userlogin
        fields = ('name','age','address','phone')


class foodaddform(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name','calories')

class mealform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model = Meal
        fields = ('foods','date')

class workoutform(forms.ModelForm):
    class Meta:
        model = workout
        fields = ('name','calories')


