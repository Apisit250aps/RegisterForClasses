from django.urls import path
from . import views as page
from django.shortcuts import render
urlpatterns = [
    path('', page.index, name='index'),
    path('about', page.about, name='about'),
]
