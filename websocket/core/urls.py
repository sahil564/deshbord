from django.urls import path
from . import views,views1
from . import consumers1

urlpatterns = [
    path("",views.index),
    path("sahil/",consumers1.sahil),
    path("", views.index, name='home1'),
    path("about/", views.about, name='about'),
    path("services/", views.services, name='services'),
    path("machine/", views.machine, name='machine'),
    path("header/",views.header, name='header'),
    path("login1/",views.login, name='login1'),
    path("log1/",views.log, name='log1'),
    path('register/',views.register,name="register"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('TVS/',views.TVS1,name="TVS"),
    path('plot/',views.test,name="plot"),
    path('sensor/',views1.sensor,name="sensor"),
    path('live/',consumers1.sahil,name="live")
]
