from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gallery_string(request):
    return HttpResponse('Thos is gallery string')

def gallery(request):
    return render(request, 'gallery.html')
    