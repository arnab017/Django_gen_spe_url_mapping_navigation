from django.urls import path
from app3.views import *

app_name = 'app3'

urlpatterns = [
    path('services_string/',services_string,name='services_string'),
    path('services/',services,name='services'),
]