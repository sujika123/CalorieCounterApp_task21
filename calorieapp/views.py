from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from calorieapp.forms import LoginForm, userloginform, foodaddform, workoutform
from calorieapp.models import userlogin, Food, Meal, workout, Work


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form = LoginForm()
    form1 = userloginform()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form1 = userloginform(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():
            user = form.save(commit=False)
            user.is_user = True
            user.save()
            tcr = form1.save(commit=False)
            tcr.user = user
            tcr.save()
            return redirect("loginview")
    return render(request,'registration.html',{'form':form,'form1':form1})

def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_staff:
            login(request,user)
            return redirect('adminhome')
        if user is not None and user.is_user:
            login(request,user)
            return redirect('userhome')
        else:
            messages.info(request,'Invalid credentials')
    return render(request,'login.html')

def adminhome(request):
    return render(request,'admin/dash.html')

def userhome(request):
    return render(request,'user/dash.html')

def profileview(request):
    u= request.user
    data = userlogin.objects.filter(user=u)
    print(data)
    return render(request,'user/profileview.html',{'data':data})

def profileupdate(request,id):
    user = userlogin.objects.get(id=id)
    form = userloginform(instance=user)
    if request.method == 'POST':
        form = userloginform(request.POST or None,request.FILES,instance=user or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return redirect('profileview')
    return render(request,'user/profileupdate.html',{'form':form})


# Calorie

def addfooditem(request):
    form = foodaddform()
    u = request.user
    if request.method == 'POST':
        form = foodaddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_fooditem')
    return render(request,'admin/addfood.html',{'form':form})


def view_fooditem(request):
    # Display list of available foods
    foods = Food.objects.all()
    return render(request, 'admin/viewFood.html', {'foods': foods})

def deletefood(request,id):
    data = Food.objects.get(id=id)
    data.delete()
    return redirect('view_fooditem')

# def add_meal(request):
#     # Add a meal for the logged-in user
#     if request.method == 'POST':
#         selected_foods = request.POST.getlist('foods')
#         date = request.POST.get('date')
#
#         user = request.user
#         meal = Meal.objects.create(user=user, date=date)
#         meal.foods.add(*selected_foods)
#
#     return render(request, 'user/CalculateCalorie.html', {'foods': Food.objects.all()})


def add_meal(request):
    if request.method == 'POST':
        selected_food_ids = request.POST.getlist('foods')
        date = request.POST.get('date')

        selected_foods = Food.objects.filter(id__in=selected_food_ids)
        total_calories = sum(food.calories for food in selected_foods)

        user = request.user
        meal = Meal.objects.create(user=user, date=date)
        meal.foods.add(*selected_foods)

        return render(request, 'user/TotalCalorie.html', {'total_calories': total_calories})

    return render(request, 'user/CalculateCalorie.html', {'foods': Food.objects.all()})


def view_userfooditem(request):
    # Display list of available foods
    foods = Food.objects.all()
    return render(request, 'user/viewAvailableFood.html', {'foods': foods})


def addwork(request):
    form = workoutform()
    u = request.user
    if request.method == 'POST':
        form = workoutform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('view_work')
    return render(request,'admin/addwork.html',{'form':form})



def view_work(request):
    # Display list of available foods
    data = workout.objects.all()
    return render(request, 'admin/viewwork.html', {'data': data})

def deletework(request,id):
    data = workout.objects.get(id=id)
    data.delete()
    return redirect('view_work')


def view_userwork(request):
    # Display list of available foods
    data = workout.objects.all()
    return render(request, 'user/viewWorkoutSession.html', {'data': data})


def add_work(request):
    if request.method == 'POST':
        selected_work_ids = request.POST.getlist('works')
        date = request.POST.get('date')

        selected_works = workout.objects.filter(id__in=selected_work_ids)
        total_calories = sum(work.calories for work in selected_works)

        user = request.user
        meal = Work.objects.create(user=user, date=date)
        meal.works.add(*selected_works)

        return render(request, 'user/TotalWorkCalorie.html', {'total_calories': total_calories})

    return render(request, 'user/CalculateWorkCalorie.html', {'works': workout.objects.all()})

