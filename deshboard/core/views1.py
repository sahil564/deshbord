from multiprocessing import context
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect 

# Create your views here.

def sensor(request):
    return render(request, 'base.html')
    # return HttpResponse("this is homepage")
    
def stop(request):
    return render(request,"stop.html")

def delete(request):
    return render(request,"Mdelete.html")

def newd(request):
    return render(request,'bar.html')
    

def newd1(request):
    return render(request,'future.html')
    