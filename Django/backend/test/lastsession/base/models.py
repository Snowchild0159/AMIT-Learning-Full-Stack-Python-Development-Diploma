from django.db import models

# Create your models here.
class Student(models.Model) : 
    name = models.CharField(max_length=200) 
    gpa = models.FloatField()
    role = models.CharField(default='regular', max_length=200)