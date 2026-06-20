from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.IntegerField()
    emp_name = models.CharField(max_length=30)
    emp_department = models.CharField(max_length=25)