from multiprocessing import context
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect 
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from core.models import TVS #add this
# Create your views here.
# from .models import *
from .forms import *
# from .filters import OrderFilter


from email import message
from django.shortcuts import render, redirect
from pyexpat.errors import messages
from wsgiref.util import request_uri
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib import messages














# Create your views here.
def index(request):
    return render(request, 'home.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'header.html') 

def services(request):
    return render(request, 'desborad.html')

# def machine(request):
def machine(request):
    # Define X and Y variable data
    x = np.array([1, 2, 3, 4])
    y = x*2
    plt.plot(x, y)
    plt.xlabel("X-axis")  # add X-axis label
    plt.ylabel("Y-axis")  # add Y-axis label
    plt.title("MODEL PERFORMANCE")  # add tit

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'machine.html',{'graphic':graphic})
    # return render(request, 'machine.html')
 

def header(request):
    return render(request, 'Mheader.html')


def login(request):
    
    return render(request,"login1.html")



def log(request):
    return render(request,"log.html")



def home(request):
    return render(request,"home.html")


def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST["last_name"]
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already exits")
                # return redirect(register)
            else:
                user=User.objects.create(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.set_password(password)
                user.save()
                context={'orgnization':username,
                         "username":first_name}
                return render(request,'desborad.html',context)
    else:
        print("this is not post request")
        return render(request,"register.html")



# def login_user(request):
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect("services")

#         else:
#             messages.info(request,'Ivalid Username or Password')
#             return redirect("login_user")

#     else:
#         return render(request,'login.html')

# def login_user(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
#             if user is not None:
#                 auth.login(request,user)
#                 return redirect("services")

#             else:
#                 messages.info(request,'Ivalid Username or Password')
#                 return redirect("login_user")

# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="login.html")

def login_user(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                context={'orgnization':password,
                         "username":username,}
                return render(request,'desborad.html',context)
            else:
                messages.info(request,"Invalid Username or password")

        else:
            messages.error(request,"Invalid username or password.")


    form=AuthenticationForm
    return render(request=request,template_name="login.html")




def logout_user(request):
    auth.logout(request)
    return redirect("home")

from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def test(request): 
    # Define X and Y variable data
    x = np.array([1, 2, 3, 4])
    y = x*2
    plt.plot(x, y)
    plt.xlabel("X-axis")  # add X-axis label
    plt.ylabel("Y-axis")  # add Y-axis label
    plt.title("Any suitable title")  # add tit

    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    return render(request, 'index111.html',{'graphic':graphic})


def TVS1(request):
    if request.POST:
        form = TVS(request.POST or None)
        # form=TVS(request.POST)
        if form.is_valid():
            form.save()
            return redirect(machine)
            
    #     username=request.POST['username']
    #     password=request.POST["password"]
    #     email=request.POST["email"]
    #     machine_ID=request.POST["machine_ID"]
    #     machine_IDC=request.POST["machine_IDC"]
    #     sensor=request.POST["sensor"]
    #     sensorname=request.POST["sensorname"]
    #     phone=request.POST["phone"]
        
    #     if machine_ID==machine_IDC:
    #         if Machines.data(machine_ID!=machine_IDC):
    #             messages.info(request,"Machine is already exits")
    #             return redirect('machine')
    #         else:
    #             user=Machines.objects.create(username=username,password=password,email=email,machine_ID=machine_ID,machine_IDC=machine_IDC,sensor=sensor,sensorname=sensorname,phone=phone)
    #             user.set_password(machine_ID)
    #             user.save()
    #             return redirect(newmachine)
    else:
        print("this is not post request")
     
        return render(request,"create_new_m.html")

































































# def registerPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('register')
# 	else:
# 		form = CreateUserForm()
# 		if request.method == 'POST':
# 			form = CreateUserForm(request.POST)
# 			if form.is_valid():
# 				form.save()
# 				user = form.cleaned_data.get('username')
# 				messages.success(request, 'Account was created for ' + user)

# 				return redirect('login')
			

# 		context = {'form':form}
# 		return render(request, 'register.html', context)

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('register')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home1')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'login.html', context)


# def logoutUser(request):
# 	logout(request)
# 	return redirect('register')

