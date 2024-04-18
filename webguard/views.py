# myapp/views.py
import os  # Import the os module
from django.shortcuts import render

def homepage(request):
    return render(request, 'webguard/homepage.html')
