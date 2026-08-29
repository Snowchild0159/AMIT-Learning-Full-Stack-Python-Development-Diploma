from django.db import models

# Create your models here.
class Department(models.Model) : 
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    manager = models.OneToOneField('Employee' , on_delete=models.SET_NULL , null=True)
    class Meta : 
        db_table = 'Department'
        
    def __str__(self):
        return  self.name   

class Employee(models.Model) : 
    name = models.CharField(max_length=200)
    gpa = models.FloatField(null=False)
    dob = models.DateField()
    address = models.TextField()
    level = models.IntegerField(null=True)
    dept_id = models.ForeignKey(Department , on_delete=models.CASCADE)
    class Meta : 
        db_table = 'Emploee'

class Project(models.Model) : 
    name =models.CharField(max_length=100)
    employee = models.ManyToManyField(Employee , through = 'EmployeeProjects')   
    
         
class EmployeeProjects(models.Model) : 
    employee =models.ForeignKey(Employee , on_delete=models.CASCADE)
    Project =models.ForeignKey(Project , on_delete=models.CASCADE)


class Student(models.Model) : 
    name = models.CharField(max_length=200)
    gpa = models.FloatField(null=False)
    dob = models.DateField()
    address = models.TextField()
    level = models.IntegerField(null=True)
    dept_id = models.ForeignKey(Department , on_delete=models.CASCADE)
    class Meta : 
        constraints = [models.CheckConstraint(condition=models.Q(gpa__lte = 4) & models.Q(gpa__gt = 0) , name="check_valie_gpa")]