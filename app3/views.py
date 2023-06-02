from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def services_string(request):
    return HttpResponse('This is services string')

def services(request):
    return render(request, 'services.html')