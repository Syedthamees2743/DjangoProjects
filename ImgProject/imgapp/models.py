from django.db import models

# Create your models here.

class Image(models.Model):
    prodname = models.CharField(max_length=100)
    proddes = models.CharField(max_length=100)
    prodprc = models.IntegerField()
    image = models.ImageField(upload_to="image/")
