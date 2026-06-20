from django.db import models

# Create your models here.


class Studentmail(models.Model):
    studentid = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    mail = models.TextField()
