# webguard/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('second-page/', views.second_page, name='second_page'),
]
