# webguard/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'webguard/homepage.html')
