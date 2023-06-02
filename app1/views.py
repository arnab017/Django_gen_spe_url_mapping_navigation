from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_string(request):
    return HttpResponse('This is my home page')

def home(request):
    return render(request, 'home.html')
