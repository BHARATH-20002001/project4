from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return render(request,'virat.html')

def maxwell(request):
    return HttpResponse('<center><h1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>maxwell<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<</h1></center>')