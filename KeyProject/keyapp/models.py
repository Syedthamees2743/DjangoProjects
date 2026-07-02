from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    course_fees = models.IntegerField()


class Student(models.Model):
    student_name = models.CharField(max_length=100)

    student_email = models.EmailField()

    student_phone = models.CharField(max_length=10)

    student_address = models.TextField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    Join_Date = models.DateField(auto_now_add=True)
