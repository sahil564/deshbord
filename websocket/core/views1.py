from multiprocessing import context
from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect 

# Create your views here.

def sensor(request):
    return render(request, 'sensor.html')
    # return HttpResponse("this is homepage")

