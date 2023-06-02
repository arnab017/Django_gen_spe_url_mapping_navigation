from django.urls import path
from app2.views import *

app_name = 'app2'

urlpatterns = [
    path('about_string/',about_string,name='about_string'),
    path('about/',about,name='about'),
]