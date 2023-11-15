from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def rohit(request):
    return render(request,'rohit.html')

def suryakumar(request):
    return HttpResponse('<center><h1>batsman</h1></center>')