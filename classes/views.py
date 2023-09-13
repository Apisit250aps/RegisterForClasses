# django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# django-rest-framework
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# app
from . import models
from . import serializers



# Create your views here.

def setData(data):
    class_info = []
    for cls in data:
        cls = dict(cls)
        # print((cls['class_category']))
        cls["class_category"] = models.Category.objects.get(id=int(cls['class_category'])).category
        class_info.append(cls)
    
    return class_info

@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def getAllClasses(request):
    status = True
    classes = models.Classes.objects.order_by('-on_register', 'class_year', 'semester')
    
    classes_data = serializers.ClassesSerializer(classes, many=True).data
    data = setData(classes_data)
        
    return Response(
        {
            "status":status,
            "data":data
        }
    )
    
@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def getCategory(request):
    status = True
    id = request.data['id']
    category = models.Category.objects.get(id=id)
    classes = models.Classes.objects.filter(class_category=category).order_by('-on_register', 'class_year', 'semester')
    
    classes_data = serializers.ClassesSerializer(classes, many=True).data
    data = setData(classes_data)
    
    return Response(
        {
            "status":status,
            "data":data,
            "category":category.category
        }
    )

@csrf_exempt
@api_view(["POST", ])
@permission_classes((AllowAny,))
def getStatus(request):
    status = True
    on_regis = int(request.data['status'])
    
    classes = models.Classes.objects.filter(on_register=on_regis).order_by('-on_register', 'class_year', 'semester')
    
    classes_data = serializers.ClassesSerializer(classes, many=True).data
    data = setData(classes_data)
    
    return Response(
        {
            "status":status,
            "data":data
        }
    )
