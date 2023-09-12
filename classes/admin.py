from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category'
    ]

@admin.register(models.Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = [
        'class_id',
        'class_name',
        'class_category',
        'on_register',
    ]