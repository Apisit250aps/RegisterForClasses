# django
from django.urls import path

# app 
from . import views as api



urlpatterns = [
    path('get/classes', api.getAllClasses, name='api-get-classes'),
    path('get/category', api.getCategory, name='api-get-cats'),
    path('get/status', api.getStatus, name='api-get-status'),
]