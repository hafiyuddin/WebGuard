# webguard/views.py
from django.shortcuts import render

def homepage(request):
    return render(request, 'webguard/homepage.html')
def second_page(request):
    return render(request, 'webguard/second_page.html')