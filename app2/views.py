from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about_string(request):
    return HttpResponse('This is about page string')

def about(request):
    return render(request, 'about.html')