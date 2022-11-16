from atexit import register
from django.contrib import admin
from django.urls import path
from core import views, views1

urlpatterns = [
	# path('register/', views.registerPage, name="register"),
	# path('login/', views.loginPage, name="login"),  
	# path('logout/', views.logoutUser, name="logout"),


    path("", views.index, name='home1'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("services1/", views.services1, name='services1'),
    path("machine/", views.machine, name='machine'),
    path("header/",views.header, name='header'),
    path("login1/",views.login, name='login1'),
    path("log1/",views.log, name='log1'),
    path('register/',views.register,name="register"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('TVS/',views.TVS1,name="TVS"),
    path('plot/',views.test,name="plot"),
    path('plot/',views.test,name="plot"),
    path('sensor/',views1.sensor,name="sensor"),
    path('stop/',views1.stop,name="stop"),
    path('delete/',views1.delete,name="delete"),
    path("base/",views.base,name="base"),
    path("base1/",views1.newd,name="base1"),
    path("base11/",views1.newd1,name="base11")
   
    
    
    
    
]
    
