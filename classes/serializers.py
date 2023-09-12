from rest_framework import serializers

from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models. Category
        fields = '__all__'
        
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Classes
        fields = '__all__'
        
