from django.db import models

class Employeemail(models.Model): 
    employeeid = models.CharField(max_length=50)
    employeename=models.CharField(max_length=50, default="Employee")
    subject = models.CharField(max_length=200)
    mail = models.EmailField(max_length=100)