from django.db import models
# from datetime import datetime
# datetime(year=2026 , month= 12 , day=3)
# Create your models here.

class Department(models.Model) : 
    name = models.CharField(max_length=200) 
    city = models.CharField(max_length=200)
    streat = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    manager = models.OneToOneField('Employee' , on_delete=models.SET_NULL , null=True)
    is_delete = models.BooleanField(default=False)
    def __str__(self) : 
        return self.name
    class Meta : 
        db_table = 'Department'
     
class Employee(models.Model) :
    name = models.CharField(max_length=200) 
    gpa = models.FloatField(null=False)
    dob = models.DateField()
    address = models.TextField() 
    username= models.CharField(max_length=250 , unique=True)
    level = models.IntegerField(null=True )
    dept_id = models.ForeignKey(Department , on_delete=models.CASCADE)
    
    def __str__(self) : 
        return self.name
    class Meta : 
        db_table = "Employee"
        
        
        constraints = [
            models.CheckConstraint(condition=models.Q(gpa__lte = 4)
                                   &models.Q(gpa__gt = 0) 
                                   , name="check_valie_gpa")
      
        ]

class Project(models.Model) : 
    name = models.CharField(max_length=100) 
    employees = models.ManyToManyField(Employee , through='EmployeePrjects')
    
class EmployeePrjects (models.Model) : 
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    project = models.ForeignKey(Project , on_delete=models.CASCADE) 
    hours = models.FloatField()
    
class Student(models.Model) :
    name = models.CharField(max_length=200) 
    gpa = models.FloatField(null=False)
    dob = models.DateField()
    address = models.TextField() 
    level = models.IntegerField(null=True )
    dept_id = models.ForeignKey(Department , on_delete=models.CASCADE)
    
    
#  python .\manage.py makemigrations
#  python .\manage.py migrate
# python manage.py shell
# from students.models import Department
    