# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Define the root URL pattern
    path('second-page/', views.second_page, name='second_page'),
]
