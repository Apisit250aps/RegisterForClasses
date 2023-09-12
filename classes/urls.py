# django
from django.urls import path

# app 
from . import views as api



urlpatterns = [
    path('get/classes', api.getAllClasses, name='api-get-classes')
]