from django.urls import path

from calorieapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register', views.register, name='register'),
    path('loginview', views.loginview, name='loginview'),
    path('userhome', views.userhome, name='userhome'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('profileview',views.profileview,name='profileview'),
    path('profileupdate/<int:id>/',views.profileupdate,name='profileupdate'),
    path('addfooditem', views.addfooditem, name='addfooditem'),
    path('view_fooditem', views.view_fooditem, name='view_fooditem'),
    path('deletefood/<int:id>/',views.deletefood,name='deletefood'),
    path('add_meal', views.add_meal, name='add_meal'),
    path('view_userfooditem', views.view_userfooditem, name='view_userfooditem'),
    path('addwork', views.addwork, name='addwork'),
    path('view_work', views.view_work, name='view_work'),
    path('view_userwork', views.view_userwork, name='view_userwork'),
    path('deletework/<int:id>/', views.deletework, name='deletework'),
    path('add_work', views.add_work, name='add_work'),

    ]