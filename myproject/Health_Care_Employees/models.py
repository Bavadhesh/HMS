from django.db import models
from django.db import models
# Create your models here.
class Employee(models.Model) :
    class Meta:
        db_table = 'Employee'
    Employee_Id = models.BigIntegerField(default=9000)
    Name = models.CharField(max_length=50)
    Designation = models.CharField(max_length=300)
    joined_date = models.DateField()
    Email_id = models.CharField(max_length=100)
    Contact_no = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    profile_photo = models.ImageField()

class EmployeeAuth(models.Model):
    class Meta:
        db_table = 'EmployeeAuth'
    Employee_Id = models.BigIntegerField()
    Email_id = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
