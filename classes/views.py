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


@csrf_exempt
@api_view(["GET", ])
@permission_classes((AllowAny,))
def getAllClasses(request):
    status = True
    classes = models.Classes.objects.all()
    
    classes_data = serializers.ClassesSerializer(classes, many=True).data
    class_info = []
    for cls in classes_data:
        cls = dict(cls)
        # print((cls['class_category']))
        cls["class_category"] = models.Category.objects.get(id=int(cls['class_category'])).category
        class_info.append(cls)
        
    return Response(
        {
            "status":status,
            "data":class_info
        }
    )
    