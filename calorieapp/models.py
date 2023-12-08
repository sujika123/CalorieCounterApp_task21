from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)

class userlogin(models.Model):
    user = models.ForeignKey(Login,on_delete = models.CASCADE,related_name = 'user',null=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    address = models.TextField(max_length=150)

    def __str__(self):
        return self.name

class Food(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Meal(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food, related_name='meals')
    date = models.DateField()

    def total_calories(self):
        return sum(food.calories for food in self.foods.all())

    def __str__(self):
        return f"{self.user.username}'s meal on {self.date}"


class workout(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Work(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    works = models.ManyToManyField(workout, related_name='works')
    date = models.DateField()

    def total_calories(self):
        return sum(work.calories for work in self.works.all())

    def __str__(self):
        return f"{self.user.username}'s wor on {self.date}"

