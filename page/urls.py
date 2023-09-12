from django.urls import path
from . import views as page
from django.shortcuts import render
urlpatterns = [
    path('', page.index),
]
