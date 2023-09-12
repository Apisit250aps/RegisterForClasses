from django.db import models

# Create your models here.

# หมวดหมู่รายวิชา
class Category(models.Model):
    category = models.CharField(max_length=128) # ชื่อหมวดหมู่วิชาเรียน

    def __str__(self):
        return self.category

# รายวิชา
class Classes(models.Model):
    class_id = models.CharField(max_length=10) # รหัสรายวิชา
    class_name = models.CharField(max_length=128) # ชื่อรายวิชา
    class_credit = models.IntegerField(max_length=1) # หน่วยกิต
    class_year = models.IntegerField(max_length=4) # ปีการศึกษา
    semester = models.IntegerField(max_length=1) # ภาคเรียน
    class_category = models.ForeignKey(Category, on_delete=models.CASCADE) # หมวดหมู่รายวิชา

    on_register = models.BooleanField(default=False) # สถานะการเปิดการลงทะเบียน

    def __str__(self):
        return self.class_name

 